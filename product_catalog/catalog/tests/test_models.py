# catalog/tests/test_models.py

from django.test import TestCase
from catalog.models import Product

class ProductModelTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=99.99,
            stock=10
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), "Test Product")

    # def test_is_in_stock_true(self):
    #     self.assertTrue(self.product.is_in_stock())

    # def test_is_in_stock_false(self):
    #     self.product.stock = 0
    #     self.assertFalse(self.product.is_in_stock())

    def test_price_field(self):
        self.assertEqual(self.product.price, 99.99)

    def test_str_method(self):
        self.assertEqual(str(self.product), "Test Product")