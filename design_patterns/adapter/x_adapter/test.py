import unittest


class Test(unittest.TestCase):

    def test_real_product(self):
        """ Стандартный интерфейс класса продукт """
        p = Product(name='SkateBoard', price=10)

        result = p.price

        self.assertEqual(10, result)

    def test_product_adapter(self):
        """ Адаптируем продукт к новому интерфейсу, использующему Каталог цен товаров """
        price_list = PriceList()
        adapter = ProductAdapter(price_list, name='SkateBoard')

        result = adapter.price

        self.assertEqual(10, result)


class PriceList:

    prices = {
        'SkateBoard': 100
    }

    def get_price(self, name):
        return self.prices[name]


