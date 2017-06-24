from examples.factory.test_8.factory import ProductFactory


def calculate_result(param):
    factory = ProductFactory()
    product = factory.make_product(param)
    if not product:
        return ''
    result = product.calculate()
    return result
