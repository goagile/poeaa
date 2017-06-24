from examples.factory.test_6.products import (
    ProductA,
    ProductB
)


class ProductFactory:
    def make_A(self):
        return ProductA()

    def make_B(self):
        return ProductB()
