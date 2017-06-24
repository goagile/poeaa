import unittest
from collections import defaultdict


def empty():
    return {
        'name': '',
        'price': 0
    }

products = defaultdict(empty)


class Test(unittest.TestCase):

    def test(self):
        expected = empty()

        result = products['key not exist']

        self.assertEqual(expected, result)
