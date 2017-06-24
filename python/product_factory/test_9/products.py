

class Product:
    def calculate(self):
        raise ValueError('Абстрактный метод')


class ProductA(Product):
    def calculate(self):
        # Большой блок вычислений
        # ...
        #
        return 'A'


class ProductB(Product):
    def calculate(self):
        # Большой блок вычислений
        # ...
        #
        return 'B'


class EmptyProduct(Product):
    def calculate(self):
        return ''
