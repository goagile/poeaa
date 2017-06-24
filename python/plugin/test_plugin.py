import unittest

from examples.python.plugin.factory import PluginFactory
from examples.python.plugin.products import ProductA, ProductB


class Test(unittest.TestCase):

    config_path = 'ng_django/examples/plugin/config.js'

    def test_get_product_A(self):
        expected = ProductA('A')
        factory = PluginFactory(config_path=self.config_path)

        product = factory.get_product_A()

        self.assertEqual(expected, product)

    def test_get_product_B(self):
        expected = ProductB('B')
        factory = PluginFactory(config_path=self.config_path)

        product = factory.get_product_B()

        self.assertEqual(expected, product)
