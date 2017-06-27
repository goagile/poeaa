import unittest
from examples.factory.test_6.app import calculate_result


class Test(unittest.TestCase):

    def test_product_a(self):
        expected = 'A'

        result = calculate_result(param=0)

        self.assertEqual(expected, result)


    def test_product_b(self):
        expected = 'B'

        result = calculate_result(param=1)

        self.assertEqual(expected, result)


    def test_empty_product(self):
        expected = ''

        result = calculate_result(param=2)

        self.assertEqual(expected, result)
