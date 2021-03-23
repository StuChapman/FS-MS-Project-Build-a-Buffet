/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                // Credit: https://stackoverflow.com/questions/24152420/pass-dynamic-javascript-variable-to-django-python
                var URL = '/checkout/create_order/';
                // From using {% csrf_token %} in the form
                var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
                var postData = {
                    'csrfmiddlewaretoken': csrfToken,
                    'paymentSuccess': 'succeeded',
                    'full_name': $.trim(form.full_name.value),
                    'email': $.trim(form.email.value),
                    'phone_number': $.trim(form.phone_number.value),
                    'country': $.trim(form.country.value),
                    'postcode': $.trim(form.postcode.value),
                    'town_or_city': $.trim(form.town_or_city.value),
                    'street_address1': $.trim(form.street_address1.value),
                    'street_address2': $.trim(form.street_address2.value),
                    'county': $.trim(form.county.value),
                    'basket_number': $.trim(form.basket_number.value),
                    'total_price': $.trim(form.total_price.value),
                };
                $.post(URL, postData);
                form.submit();
            }
        }
    });
});