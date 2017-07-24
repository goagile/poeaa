import unittest


class Test(unittest.TestCase):

    def test_real_product(self):
        """ Стандартный интерфейс класса продукт """
        expected = 100
        p = Product(name='SkateBoard', price=100)

        result = p.price

        self.assertEqual(expected, result)

    def test_product_adapter(self):
        """ Адаптируем продукт к новому интерфейсу, использующему Каталог цен товаров """
        expected = 100
        price_list = PriceList()
        adapter = ProductAdapter(price_list, name='SkateBoard')

        result = adapter.price

        self.assertEqual(expected, result)


class BaseProduct:

    @property
    def price(self):
        raise ValueError('ABS')


class Product(BaseProduct):

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price


class PriceList:

    prices = {
        'SkateBoard': 100
    }

    def get_price(self, name):
        return self.prices[name]


class ProductAdapter(BaseProduct):

    def __init__(self, price_list, name):
        self.__price_list = price_list
        self.__name = name

    @property
    def price(self):
        price = self.__price_list.get_price(self.__name)
        product = Product(self.__name, price)
        result = product.price
        return result
