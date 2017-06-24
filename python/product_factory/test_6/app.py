from examples.factory.test_6.factory import ProductFactory


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
