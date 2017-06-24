from examples.factory.test_10.products import (
    EmptyProduct,
    registry
)


class Factory:
    products = {}

    def make_product(self, param):
        product_name = self.products.get(param)
        product_class = registry.get(product_name)
        if not product_class:
            return EmptyProduct()
        return product_class()


class ProductFactory(Factory):
    products = {
        0: 'ProductA',
        1: 'ProductB'
    }
