// Validation for all forms at client end to prevent user errors or malicious behavior
// Credit: https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/

// Handle product_search_form submit

var productSearchForm = document.getElementById('product_search_form');
var productSearchEl = document.getElementById('product_search');

const isSearchRequired = value => value === '' ? false : true;
const isSearchText = (string) => {
    const re = new RegExp(/^[a-zA-Z ]+$/);
    return re.test(string);
};

const checkProductSearchForm = () => {

    let searchValid = false;
    const min = 2,
        max = 25;
    const productSearch = productSearchEl.value.trim();

    if (!isSearchRequired(productSearch)) {
        $('#validation_alerts').html('<i class="fas fa-exclamation-triangle"></i> Search cannot be blank.');
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    } else if (!isSearchText(productSearch)) {
        $('#validation_alerts').html('<i class="fas fa-exclamation-triangle"></i> Search must be text only.');
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    } else {
        searchValid = true;
    }
    return searchValid;
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

// Handle user-question-form submit

var userQuestionForm = document.getElementById('user-question-form');
var userQuestionName = document.getElementById('user-question-name');
var userQuestionEmail = document.getElementById('user-question-email');
var userQuestionQuestion = document.getElementById('user-question-question');

const isQuestionRequired = value => value === '' ? false : true;
const isQuestionText = (string) => {
    const re = new RegExp(/^[a-zA-Z ]+$/);
    return re.test(string);
};
const isQuestionEmailValid = (email) => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

const checkUserQuestionForm = () => {

    let questionValid = false;
    const min = 2,
        max = 25;
    const questionName = userQuestionName.value.trim();
    const questionEmail = userQuestionEmail.value.trim();
    const questionQuestion = userQuestionQuestion.value.trim();

    if (!isQuestionRequired(questionName)) {
        $('#validation_alerts').html('<i class="fas fa-exclamation-triangle"></i> Name cannot be blank.');
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    } else if (!isQuestionText(questionName)) {
        $('#validation_alerts').html('<i class="fas fa-exclamation-triangle"></i> Name must contain only letters, numbers, and @/./+/-/_ characters.');
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    } else if (!isQuestionEmailValid(questionEmail)) {
        $('#validation_alerts').html('<i class="fas fa-exclamation-triangle"></i> Email must be in a valid format.');
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    } else if (!isQuestionRequired(questionQuestion)) {
        $('#validation_alerts').html('<i class="fas fa-exclamation-triangle"></i> Question cannot be blank.');
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    } else if (!isQuestionText(questionQuestion)) {
        $('#validation_alerts').html('<i class="fas fa-exclamation-triangle"></i> Question must contain only letters, numbers, and @/./+/-/_ characters.');
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    } else {
        questionValid = true;
    }
    return questionValid;
}

userQuestionForm.addEventListener('submit', function(ev) {
    ev.preventDefault();

    // validate forms
    let isUserQuestionFormValid = checkUserQuestionForm();

    let isFormValid = isUserQuestionFormValid;

    // submit to the server if the form is valid
    if (isFormValid) {
        userQuestionForm.submit();
    }

});