import json

from examples.plugin.products import ProductA, ProductB


class PluginFactory:

    def __init__(self, config_path=''):
        self.config_path = config_path
        self.config = self.get_config()

    def get_config(self):
        result = {}
        with open(self.config_path, 'r') as f:
            result = json.loads(''.join(f.readlines()))
        return result

    def get_instance(self, name):
        class_ = self.config.get(name, None)
        product_instance = eval(class_)(name)
        return product_instance

    def get_product_A(self):
        return self.get_instance('A')

    def get_product_B(self):
        return self.get_instance('B')
