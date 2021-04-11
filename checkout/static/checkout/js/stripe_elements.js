// Credit: Code-Institute
/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Handle payment-form validation

var userIdFullName = document.getElementById('id_full_name');
var userIdEmail = document.getElementById('id_email');
var userIdPhoneNumber = document.getElementById('id_phone_number');
var userIdStreetAddress1 = document.getElementById('id_street_address1');
var userIdStreetAddress2 = document.getElementById('id_street_address2');
var userIdTownOrCity = document.getElementById('id_town_or_city');
var userIdCounty = document.getElementById('id_county');
var userIdPostcode = document.getElementById('id_postcode');

const isPaymentText = (string) => {
    const re = new RegExp(/^[a-zA-Z ]+$/);
    return re.test(string);
};
const isPaymentAlphaNumeric = (string) => {
    const re = new RegExp(/^[a-zA-Z _0-9?\@\.\+\-\_]+$/);
    return re.test(string);
};
const isPaymentNumerals = (number) => {
    const re = new RegExp('^[0-9]+$');
    return re.test(number);
};
const isPaymentEmailValid = (email) => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

const checkPaymentUserIdForm = () => {

    let idValid = false;
    const idFullName = userIdFullName.value.trim();
    const idEmail = userIdEmail.value.trim();
    const idPhoneNumber = userIdPhoneNumber.value.trim();
    const idStreetAddress1 = userIdStreetAddress1.value.trim();
    const idStreetAddress2 = userIdStreetAddress2.value.trim();
    const idTownOrCity = userIdTownOrCity.value.trim();
    const idCounty = userIdCounty.value.trim();
    const idPostCode = userIdPostcode.value.trim();

    // Test text fields
    if (!isPaymentText(idFullName)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Full Name must contain only letters.';
    } else if (!isPaymentAlphaNumeric(idStreetAddress1)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Address Line 1 must contain only letters and numbers.';
    } else if (!isPaymentAlphaNumeric(idStreetAddress2) && idStreetAddress2 !== "") {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Address Line 2 must contain only letters and numbers.';
    } else if (!isPaymentText(idTownOrCity)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Town or City must contain only letters.';
    } else if (!isPaymentText(idCounty) && idCounty !== "") {
        var alert = '<i class="fas fa-exclamation-triangle"></i> County must contain only letters.';
    } else if (!isPaymentAlphaNumeric(idPostCode)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Postcode must contain only letters and numbers.';
    } else if (!isPaymentNumerals(idPhoneNumber)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Phone Number must contain only numbers.';
    } else if (!isPaymentEmailValid(idEmail)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Email must be in a valid format.';
    } else {
        idValid = true;
    }
    if (alert) {
        $('#validation_alerts').html(alert);
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    }
    return idValid;
}

// Stripe payments

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

    // validate form
    let isPaymentFormValid = checkPaymentUserIdForm();

    // submit to the server if the form is valid
    if (isPaymentFormValid) {
        card.update({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
        $('#boxcheckout').fadeToggle(100);
        $('#imagepay').fadeToggle(100);
        var saveInfo = Boolean($('#id-save-info').attr('checked'));
        // From using {% csrf_token %} in the form
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        var postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
            'paymentSuccess': 'succeeded',
            'current_user': $.trim(form.current_user.value),
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

        var url = '/checkout/create_order/';

        $.post(url, postData).done(function () {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.current_user.value),
                        phone: $.trim(form.basket_number.value),
                        email: $.trim(form.email.value),
                        address:{
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            state: $.trim(form.county.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        postal_code: $.trim(form.postcode.value),
                        state: $.trim(form.county.value),
                    }
                },
            }).then(function(result) {
                if (result.error) {
                    var errorDiv = document.getElementById('card-errors');
                    var html = `
                        <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                        </span>
                        <span>${result.error.message}</span>`;
                    $(errorDiv).html(html);
                    $('#boxcheckout').fadeToggle(100);
                    $('#imagepay').fadeToggle(100);
                    card.update({ 'disabled': false});
                    $('#submit-button').attr('disabled', false);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
        }).fail(function () {
            // just reload the page, the error will be in django messages
            location.reload();
        })
    }
});
