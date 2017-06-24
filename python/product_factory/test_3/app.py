def calculate_result(param):
    if param == 0:
        product = ProductA()
        result = product.calculate()
        return result

    elif param == 1:
        # Большой блок вычислений
        # ...
        #
        return 'B'

    else:
        return ''


class ProductA:
    def calculate(self):
        # Большой блок вычислений
        # ...
        #
        return 'A'
