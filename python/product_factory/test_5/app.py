from examples.factory.test_5.products import (
    ProductA,
    ProductB
)


def calculate_result(param):
    factory = ProductFactory()

    if param == 0:
        product = factory.make_A()
        result = product.calculate()
        return result

    elif param == 1:
        product = factory.make_B()
        result = product.calculate()
        return result

    else:
        return ''


class ProductFactory:
    def make_A(self):
        return ProductA()

    def make_B(self):
        return ProductB()
