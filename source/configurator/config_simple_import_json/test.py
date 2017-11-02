import unittest
from python.configurator.config_simple_import_json.custom_configs import Product


class TestImportFromJson(unittest.TestCase):

    def test(self):
        expected = 'Black box'

        result = Product

        print(result.name.name)

        self.assertEqual(expected, result.name.name)
