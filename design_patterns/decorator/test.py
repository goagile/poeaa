import unittest

from examples.decorator.product import Product


class Test(unittest.TestCase):

    def test_raise_error(self):
        expected = 1
        product = Product()

        with self.assertRaises(ValueError):
            product.price = 1

    def test_value_in_range(self):
        expected = 10
        product = Product()
        product.price = 10

        result = product._price

        self.assertEqual(expected, result)
