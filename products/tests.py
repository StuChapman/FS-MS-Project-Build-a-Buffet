from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    def test_test(self):
        self.assertEqual(1, 1)

    def test_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
