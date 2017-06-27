from examples.factory.test_10.factory import ProductFactory


def calculate_result(param):
    product = ProductFactory().make_product(param)
    result = product.calculate()
    return result
