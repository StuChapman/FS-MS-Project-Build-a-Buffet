// Validation for all forms at client end to prevent user errors or malicious behavior
// Credit: https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/

const isRequired = value => value === '' ? false : true;

const isText = (string) => {
    const re = new RegExp(/^[a-zA-Z ]+$/);
    return re.test(string);
};
const isAlphaNumeric = (string) => {
    const re = new RegExp(/^[a-zA-Z _0-9?\@\.\+\-\_]+$/);
    return re.test(string);
};
const isNumerals = (number) => {
    const re = new RegExp('^[0-9]+$');
    return re.test(number);
};
const isEmailValid = (email) => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

// Handle product_search_form submit

var productSearchForm = document.getElementById('product_search_form');
var productSearchEl = document.getElementById('product_search');

const checkProductSearchForm = () => {

    let searchValid = false;
    const productSearch = productSearchEl.value.trim();

    if (!isRequired(productSearch)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Search cannot be blank.';
    } else if (!isAlphaNumeric(productSearch)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Search must be text or numerals only.';
    } else {
        searchValid = true;
    }
    if (alert) {
        $('#validation_alerts').html(alert);
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    }
    return searchValid;
}


if (productSearchForm !== null) {
    productSearchForm.addEventListener('submit', function(ev) {
        ev.preventDefault();

        // validate forms
        let isProductSearchFormValid = checkProductSearchForm();

        let isFormValid = isProductSearchFormValid;

        // submit to the server if the form is valid
        if (isFormValid) {
            productSearchForm.submit();
        }

    });
};

// Handle user-question-form submit

var userQuestionForm = document.getElementById('user-question-form');
var userQuestionName = document.getElementById('user-question-name');
var userQuestionEmail = document.getElementById('user-question-email');
var userQuestionQuestion = document.getElementById('user-question-question');

const checkUserQuestionForm = () => {

    let questionValid = false;
    const questionName = userQuestionName.value.trim();
    const questionEmail = userQuestionEmail.value.trim();
    const questionQuestion = userQuestionQuestion.value.trim();

    if (!isRequired(questionName)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Name cannot be blank.';
    } else if (!isAlphaNumeric(questionName)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Name must contain only letters, numbers, and @.+-_ characters.';
    } else if (!isEmailValid(questionEmail)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Email must be in a valid format.';
    } else if (!isRequired(questionQuestion)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Question cannot be blank.';
    } else if (!isAlphaNumeric(questionQuestion)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Question must contain only letters, numbers, and @.+-_ characters.';
    } else {
        questionValid = true;
    }
    if (alert) {
        $('#validation_alerts').html(alert);
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    }
    return questionValid;
}

if (userQuestionForm !== null) {
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
};

// Handle product_search_admin_form submit

var productSearchAdminForm = document.getElementById('product_search_admin_form');
var productSearchAdminEl = document.getElementById('product_search_admin');

var productAdminNameEl = document.getElementById('id_name');
var productAdminDescriptionEl = document.getElementById('id_description');

const checkProductSearchAdminForm = () => {

    let adminValid = false;
    const productSearchAdmin = productSearchAdminEl.value.trim();
    const productAdminName = productAdminNameEl.value.trim();
    console.log('productAdminName');
    console.log(productAdminName);
    const productAdminDescription = productAdminDescriptionEl.value.trim();

    if (!isRequired(productSearchAdmin)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Search cannot be blank.';
    } else if (!isAlphaNumeric(productSearchAdmin)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Search must be text or numerals only.';
    } else if (!isText(productAdminName)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Name must contain only letters.';
    } else if (!isAlphaNumeric(productAdminDescription)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
    } else {
        adminValid = true;
    }
    if (alert) {
        $('#validation_alerts').html(alert);
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    }
    return adminValid;
}

if (productSearchAdminForm !== null) {
    productSearchAdminForm.addEventListener('submit', function(ev) {
        ev.preventDefault();

        // validate forms
        let isProductSearchAdminFormValid = checkProductSearchAdminForm();

        let isFormValid = isProductSearchAdminFormValid;

        // submit to the server if the form is valid
        if (isFormValid) {
            productSearchAdminForm.submit();
        }

    });
};

// Handle product-update-form submit

var productUpdateForm = document.getElementById('product-update-form');

var productAdminNameEl = document.getElementById('id_name');
var productAdminDescriptionEl = document.getElementById('id_description');

const checkProductUpdateForm = () => {

    let adminValid = false;
    const productAdminName = productAdminNameEl.value.trim();
    const productAdminDescription = productAdminDescriptionEl.value.trim();

    if (!isText(productAdminName)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Name must contain only letters.';
    } else if (!isAlphaNumeric(productAdminDescription)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
    } else {
        adminValid = true;
    }
    if (alert) {
        $('#validation_alerts').html(alert);
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    }
    return adminValid;
}

if (productUpdateForm !== null) {
    productUpdateForm.addEventListener('submit', function(ev) {
        ev.preventDefault();

        // validate forms
        let isCheckProductUpdateFormValid = checkProductUpdateForm();

        let isFormValid = isCheckProductUpdateFormValid;

        // submit to the server if the form is valid
        if (isFormValid) {
            productUpdateForm.submit();
        }

    });
};

// Handle delete-product event

var deleteProduct = document.getElementById('delete-product');
var allowClick = false

if (deleteProduct !== null) {
    deleteProduct.addEventListener('click', function(ev) {
        if (allowClick == false) {
            ev.preventDefault();
        }

        if (document.getElementById("delete-product").innerHTML != "SURE???") {
            document.getElementById("delete-product").innerHTML = "SURE???";
            allowClick = true;
        } else if (document.getElementById("delete-product").innerHTML == "SURE???") {
            document.getElementById("delete-product").innerHTML = "delete";
        }

    });
};