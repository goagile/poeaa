from collections import defaultdict

from examples.factory.test_11.products import registry


class Factory:
    products = defaultdict(lambda: '')

    def make_product(self, param):
        product_name = self.products.get(param)
        product_class = registry[product_name]
        return product_class()


class ProductFactory(Factory):
    Factory.products.update({
        0: 'ProductA',
        1: 'ProductB'
    })
