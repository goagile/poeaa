import json
from collections import defaultdict

from examples.factory.test_12.products import registry


class Factory:
    products = defaultdict(lambda: '')

    def __init__(self, path):
        self.path = path
        self.products.update(self.load())

    def make_product(self, param):
        product_name = self.products[str(param)]
        product_class = registry[product_name]
        return product_class()

    def load(self):
        result = {}
        with open(self.path, 'r') as file:
            result = json.load(file)
        return result
