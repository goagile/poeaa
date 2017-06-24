from .factory import Factory


PATH = 'ng_django/examples/factory/test_12/products.json'


def calculate_result(param):
    product = Factory(PATH).make_product(param)
    result = product.calculate()
    return result
