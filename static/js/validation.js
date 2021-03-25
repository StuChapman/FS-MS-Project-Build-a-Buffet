// Validation for all forms at client end to prevent user errors or malicious behavior

// Handle form submit
var productSearch = document.getElementById('product_search');
console.log($('product_search').type)

productSearch.addEventListener('change', function (event) {
    console.log("working")
});