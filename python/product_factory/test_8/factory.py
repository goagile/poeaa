from examples.factory.test_8.products import (
    ProductA,
    ProductB
)


class ProductFactory:

    products = {
        0: ProductA(),
        1: ProductB()
    }

    def make_product(self, param):
        product = self.products.get(param)
        return product
