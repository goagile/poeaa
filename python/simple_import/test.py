import unittest
import examples.python.simple_import.Image


class Test(unittest.TestCase):

    def test(self):
        expected = 'IMAGE'
        image = examples.python.simple_import.Image.Image()

        result = image.get_content()

        self.assertEqual(expected, result)
