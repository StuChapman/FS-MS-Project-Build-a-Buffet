// Validation for all forms at client end to prevent user errors or malicious behavior
// Credit: https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/

const isRequired = value => value === '' ? false : true;

const isText = (string) => {
    const re = new RegExp(/^[a-zA-Z ]+$/);
    return re.test(string);
};
const isAlphaNumeric = (string) => {
    const re = new RegExp(/^[a-zA-Z _0-9?\@\.\+\,\-\_]+$/);
    return re.test(string);
};
const isNumerals = (number) => {
    const re = new RegExp('^[0-9]+$');
    return re.test(number);
};
const isDecimal = (number) => {
    const re = new RegExp(/^\d+(?:\.\d\d?)?$/);
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

const checkProductSearchAdminForm = () => {

    let adminValid = false;
    const productSearchAdmin = productSearchAdminEl.value.trim();

    if (!isAlphaNumeric(productSearchAdmin)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Search must be text or numerals only.';
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
var newDataset = document.getElementById('dataset');

var productUpdateNameEl = document.getElementById('id_name');
var productUpdateDescriptionEl = document.getElementById('id_description');
var productUpdatePriceEl = document.getElementById('id_price');
var productUpdateOptionOne = document.getElementById('id_option1');
var productUpdateOptionTwo = document.getElementById('id_option2');
var productUpdateOptionThree = document.getElementById('id_option3');
var productUpdateCategoryName = document.getElementById('id_name');
var productUpdateFriendlyName = document.getElementById('id_friendly_name');

if (newDataset !== null) {
    var dataSet = newDataset.value.trim();
}

const checkProductUpdateForm = () => {

    let UpdateValid = false;

    if (dataSet == 'products') {
        const productUpdateName = productUpdateNameEl.value.trim();
        const productUpdateDescription = productUpdateDescriptionEl.value.trim();
        const productUpdatePrice = productUpdatePriceEl.value.trim();
         if (!isText(productUpdateName)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Name must contain only letters.';
        } else if (!isAlphaNumeric(productUpdateDescription)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else if (!isDecimal(productUpdatePrice)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Price must be a number to 2 decimal places.';
        } else {
            UpdateValid = true;
        }
    }
    if (dataSet == 'options') {
        const optionOne = productUpdateOptionOne.value.trim();
        const optionTwo = productUpdateOptionTwo.value.trim();
        const optionThree = productUpdateOptionThree.value.trim();
        if (!isAlphaNumeric(optionOne)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else if (!isAlphaNumeric(optionTwo)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else if (!isAlphaNumeric(optionThree)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else {
            UpdateValid = true;
        }
    }
    if (dataSet == 'categories') {
        const categoryName = productUpdateCategoryName.value.trim();
        const friendlyName = productUpdateFriendlyName.value.trim();
        if (!isAlphaNumeric(categoryName)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else if (!isAlphaNumeric(friendlyName)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else {
            UpdateValid = true;
        }
    }
    if (alert) {
        $('#validation_alerts').html(alert);
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    }
    return UpdateValid;
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

        if (document.getElementById("delete-product").innerHTML != "CONFIRM?") {
            document.getElementById("delete-product").innerHTML = "CONFIRM?";
            $('#delete-product').css('color', 'black');
            allowClick = true;
        } else if (document.getElementById("delete-product").innerHTML == "CONFIRM?") {
            document.getElementById("delete-product").innerHTML = "delete";
            $('#delete-product').css('color', 'white');
        }

    });
};

// Handle empty_basket event

var deleteProduct = document.getElementById('empty-basket');
var allowClick = false

if (deleteProduct !== null) {
    deleteProduct.addEventListener('click', function(ev) {
        if (allowClick == false) {
            ev.preventDefault();
        }

        if (document.getElementById("empty-basket").text != "CONFIRM DELETE") {
            document.getElementById("empty-basket").text = "CONFIRM DELETE";
            $('#empty-basket').css('color', 'black');
            allowClick = true;
        }

    });
};

// Handle new-product-form submit

var newProductForm = document.getElementById('new-product-form');
var newDataset = document.getElementById('dataset');

var newProductName = document.getElementById('new_name');
var newProductDescription = document.getElementById('new_description');
var newProductPrice = document.getElementById('new_price');
var newOptionOne = document.getElementById('new_option_one');
var newOptionTwo = document.getElementById('new_option_two');
var newOptionThree = document.getElementById('new_option_three');
var newCategoryName = document.getElementById('new_category_name');
var newFriendlyName = document.getElementById('new_friendly_name');

if (newDataset !== null) {
    var dataSet = newDataset.value.trim();
}

const checkNewProductForm = () => {

    let newValid = false;

    if (dataSet == 'products') {
        const productName = newProductName.value.trim();
        const productDescription = newProductDescription.value.trim();
        const productPrice = newProductPrice.value.trim();
        if (!isText(productName)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Name must contain only letters.';
        } else if (!isAlphaNumeric(productDescription)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else if (!isDecimal(productPrice)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Price must be a number to 2 decimal places.';
        } else {
            newValid = true;
        }
    }
    if (dataSet == 'options') {
        const optionOne = newOptionOne.value.trim();
        const optionTwo = newOptionTwo.value.trim();
        const optionThree = newOptionThree.value.trim();
        if (!isAlphaNumeric(optionOne)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else if (!isAlphaNumeric(optionTwo)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else if (!isAlphaNumeric(optionThree)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else {
            newValid = true;
        }
    }
    if (dataSet == 'categories') {
        const categoryName = newCategoryName.value.trim();
        const friendlyName = newFriendlyName.value.trim();
        if (!isAlphaNumeric(categoryName)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else if (!isAlphaNumeric(friendlyName)) {
            var alert = '<i class="fas fa-exclamation-triangle"></i> Description must contain only letters, numbers, and @.+-_ characters.';
        } else {
            newValid = true;
        }
    }
    if (alert) {
        $('#validation_alerts').html(alert);
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    }
    return newValid;
}

if (newProductForm !== null) {
    newProductForm.addEventListener('submit', function(ev) {
        ev.preventDefault();

        // validate forms
        let isCheckNewProductFormValid = checkNewProductForm();

        let isFormValid = isCheckNewProductFormValid;

        // submit to the server if the form is valid
        if (isFormValid) {
            newProductForm.submit();
        }

    });
};

// Handle profile-update-form submit

var ProfileUpdateForm = document.getElementById('profile-update-form');

var userIdDefaultFullName = document.getElementById('id_default_full_name');
var userIdDefaultEmail = document.getElementById('id_default_email');
var userIdDefaultPhoneNumber = document.getElementById('id_default_phone_number');
var userIdDefaultStreetAddress1 = document.getElementById('id_default_street_address1');
var userIdDefaultStreetAddress2 = document.getElementById('id_default_street_address2');
var userIdDefaultTownOrCity = document.getElementById('id_default_town_or_city');
var userIdDefaultCounty = document.getElementById('id_default_county');
var userIdDefaultPostcode = document.getElementById('id_default_postcode');

const checkProfileUpdateForm = () => {

    let idProfileValid = false;
    const idFullName = userIdDefaultFullName.value.trim();
    const idPhoneNumber = userIdDefaultPhoneNumber.value.trim();
    const idStreetAddress1 = userIdDefaultStreetAddress1.value.trim();
    const idStreetAddress2 = userIdDefaultStreetAddress2.value.trim();
    const idTownOrCity = userIdDefaultTownOrCity.value.trim();
    const idCounty = userIdDefaultCounty.value.trim();
    const idPostCode = userIdDefaultPostcode.value.trim();

    // Test text fields
    if (!isText(idFullName)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Full Name must contain only letters.';
    } else if (!isAlphaNumeric(idStreetAddress1)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Address Line 1 must contain only letters and numbers.';
    } else if (!isAlphaNumeric(idStreetAddress2) && idStreetAddress2 !== "") {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Address Line 2 must contain only letters and numbers.';
    } else if (!isText(idTownOrCity)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Town or City must contain only letters.';
    } else if (!isText(idCounty) && idCounty !== "") {
        var alert = '<i class="fas fa-exclamation-triangle"></i> County must contain only letters.';
    } else if (!isAlphaNumeric(idPostCode)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Postcode must contain only letters and numbers.';
    } else if (!isNumerals(idPhoneNumber)) {
        var alert = '<i class="fas fa-exclamation-triangle"></i> Phone Number must contain only numbers.';
    } else {
        idProfileValid = true;
    }
    if (alert) {
        $('#validation_alerts').html(alert);
        // Credit: https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide
        $("#validation_alerts").show("slow").delay(2000).hide("slow");
    }
    return idProfileValid;
}

if (ProfileUpdateForm !== null) {
    ProfileUpdateForm.addEventListener('submit', function(ev) {
        ev.preventDefault();

        // validate forms
        let ischeckProfileUpdateFormValid = checkProfileUpdateForm();

        let isFormValid = ischeckProfileUpdateFormValid;

        // submit to the server if the form is valid
        if (isFormValid) {
            ProfileUpdateForm.submit();
        }

    });
};