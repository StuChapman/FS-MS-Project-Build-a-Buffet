// Validation for all forms at client end to prevent user errors or malicious behavior
// Credit: https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/

// Handle form submit
var productSearchForm = document.getElementById('product_search_form');
var productSearchEl = document.getElementById('product_search');

const isRequired = value => value === '' ? false : true;
const isText = (string) => {
    const re = new RegExp("[a-zA-Z]");
    return re.test(string);
};

const checkProductSearchForm = () => {

    let valid = false;
    const min = 2,
        max = 25;
    const productSearch = productSearchEl.value.trim();

    if (!isRequired(productSearch)) {
        $('#validation_alerts').text('Search cannot be blank.');
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    } else if (!isText(productSearch)) {
        $('#validation_alerts').text('Search must be text only.');
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    } else {
        valid = true;
    }
    return valid;
}

productSearchForm.addEventListener('submit', function(ev) {
    ev.preventDefault();
    // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide

    // validate forms
    let isProductSearchFormValid = checkProductSearchForm();

    let isFormValid = isProductSearchFormValid;

    // submit to the server if the form is valid
    if (isFormValid) {
        productSearchForm.submit();
    }

});

