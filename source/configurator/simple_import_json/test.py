import unittest


class TestImportFromJson(unittest.TestCase):

    def test(self):
        from python.configurator.simple_import_json.domain import product
        expected = {
            'name': 'Black box'
        }

        result = product

        self.assertEqual(expected, result)
