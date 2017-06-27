from examples.python.config.base_test import BaseTestCase
from examples.python.config.products import Products

from python.configurator.config.config import Config


class TestClassAsValueCollection(BaseTestCase):

    def test_get_attribute(self):
        self.assertCasesEqual(cases=[
            ('Велотренажер',    Products.Velo.label),
            ('Водный мотоцикл', Products.Aqua.label)
        ])

    def test_set_attribute(self):
        self.assertEqual('Велотренажер', Products.Velo.label)
        Products.Velo.label = 'Велорикша'
        self.assertEqual('Велорикша', Products.Velo.label)

    def test_equal(self):
        self.assertConditionsAreTrue(conditions=[
            (True,  Products.Velo == Products.Velo),
            (False, Products.Aqua == Products.Velo)
        ])


class TestInstanceAsDynamicConfig(BaseTestCase):

    def test_load_from_json_file(self):
        path = 'ng_django/examples/config/products.json'

        config = Products.parse_json(path)

        self.assertCasesEqual(cases=[
            ('Велотренажер',    config.Velo.label),
            ('Водный мотоцикл', config.get('Aqua').label)
        ])

    def test_load_to_json_file(self):
        path = 'ng_django/examples/config/products.json'
        expected_config = Products.parse_json(path)

        export_path = 'ng_django/examples/config/products_export.json'
        expected_config.export_json(export_path)

        result = Config.parse_json(export_path)

        self.assertEqual(expected_config, result)

    def test_generate_py_file(self):
        path_json = 'ng_django/examples/config/products.json'
        path_py = 'ng_django/examples/config/products_gen.py'
        config = Products.parse_json(path_json)

        config.generate_py_file(path_py)
