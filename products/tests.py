from django.test import TestCase

import re

# Create your tests here.


class TestViews(TestCase):

    def test_test(self):
        self.assertEqual(1, 1)

    def test_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_category_product(self):

        category_product = 'category,product_name,selected-one'
        category_product_list = category_product.split(',')
        category = category_product_list[0]
        product = category_product_list[1]
        selected = category_product_list[2]

        self.assertEqual(category, 'category')
        self.assertEqual(product, 'product_name')
        self.assertEqual(selected, 'selected-one')

    def test_product_search_validation_letter(self):

        userVal = "a"
        if re.match("^[a-zA-Z0-9*]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_product_search_validation_number(self):

        userVal = "9"
        if re.match("/^[a-zA-Z ]+$/", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    def test_product_search_validation_special(self):

        userVal = "<"
        if re.match("/^[a-zA-Z ]+$/", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    def test_product_search_validation_space(self):

        userVal = "and a"
        if re.match("/^[a-zA-Z ]+$/", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_product_search_validation_asterisk(self):

        userVal = "*"
        if re.match("/^[a-zA-Z ]+$/", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)
