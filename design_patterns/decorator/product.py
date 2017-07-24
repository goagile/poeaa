from examples.decorator.utils import prop, is_in_range


@prop('price', is_in_range(minimum=10, maximum=100))
class Product(object):

    def __init__(self):
        pass
