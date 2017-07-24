import unittest


class Test(unittest.TestCase):

    def test_real_product_get_price(self):
        expected = 10
        product = ProductImpl(product_id=1, name='Beatbox', price=10)

        result = product.price

        self.assertEqual(expected, result)

    def test_proxy_product_get_price(self):
        expected = 10
        product = ProductProxy(product_id=1)

        result = product.price

        self.assertEqual(expected, result)
