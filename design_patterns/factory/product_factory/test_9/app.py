from examples.factory.test_9.factory import ProductFactory


def calculate_result(param):
    factory = ProductFactory()
    product = factory.make_product(param)
    result = product.calculate()
    return result
