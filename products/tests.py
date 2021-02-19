from django.test import TestCase, RequestFactory

from .models import Product, Category, Options
from .views import product_detail

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

    def test_product_detail(self):
        self.factory = RequestFactory()

        # Create an instance of a GET request.
        request = self.factory.post(
            {
                'category': 'sandwiches',
                'product': 'cheese'
            }
        )

        # Test my_view() as if it were deployed at /customer/details
        response = product_detail(request)
        self.assertEqual(response.status_code, 200)
