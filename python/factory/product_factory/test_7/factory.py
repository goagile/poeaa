from examples.factory.test_7.products import (
    ProductA,
    ProductB
)


class ProductFactory:

    def make_product(self, param):
        if param == 0:
            return ProductA()
        elif param == 1:
            return ProductB()
        else:
            return ''
