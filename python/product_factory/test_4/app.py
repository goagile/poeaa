from examples.factory.test_4.products import ProductA, ProductB


def calculate_result(param):
    if param == 0:
        product = ProductA()
        result = product.calculate()
        return result

    elif param == 1:
        product = ProductB()
        result = product.calculate()
        return result

    else:
        return ''
