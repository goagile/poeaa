from collections import defaultdict


registry = defaultdict(lambda: EmptyProduct)


def register_class(klass):
    registry[klass.__name__] = klass


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls


class Product(metaclass=Meta):
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
