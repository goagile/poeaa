import unittest


class Test(unittest.TestCase):

    def test_real_product_get_price(self):
        expected = 10
        product = ProductImpl(product_id=1, name='Beatbox', price=10)

        result = product.price

        self.assertEqual(expected, result)

    def test_proxy_product_get_price(self):
        DB.add_product(product_id=1, name='Beatbox', price=10)
        expected = 10
        product = ProductProxy(product_id=1)

        result = product.price

        self.assertEqual(expected, result)


class ProductImpl:

    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price


class ProductProxy:

    def __init__(self, product_id):
        self.__product_id = product_id

    @property
    def price(self):
        dict_ = DB.get_product(self.__product_id)
        p = ProductImpl(
            self.__product_id,
            dict_.get('name'),
            dict_.get('price')
        )
        return p.price


class DB:

    products = {}

    @classmethod
    def add_product(cls, product_id, name, price):
        cls.products[product_id] = {
            'name': name,
            'price': price
        }

    @classmethod
    def get_product(cls, product_id):
        return cls.products.get(product_id)
