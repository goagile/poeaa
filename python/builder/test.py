import json
import unittest


class TestJSONBuilder(unittest.TestCase):

    def make(self):
        return Builder()

    def test_add_name(self):
        expected = {
            'Product': []
        }
        builder = self.make()

        result = builder.add_name('Product').items

        self.assertEqual(expected, result)

    def test_add_field_param(self):
        expected = {
            'Product': [{
                'name': 'Kg',
                'label': 'Килограмм'
            }]
        }
        builder = self.make()
        builder.add_name('Product')

        result = builder.add_field(name='Kg', label='Килограмм').items

        self.assertEqual(expected, result)

    def test_json_builder(self):
        builder = JsonBuilder()

        builder.add_name('Products')
        builder.add_field(name='Kg', label='Килограмм')

        builder.save(path='ng_django/examples/builder/products.json')


class Builder:

    def __init__(self):
        self.name = ''
        self.items = {}

    def add_name(self, name):
        self.name = name
        self.items[self.name] = []
        return self

    def add_field(self, **kwargs):
        self.items[self.name].append(kwargs)
        return self


class JsonBuilder(Builder):

    def save(self, path):
        with open(path, 'w') as file:
            json.dump(self.items, fp=file, ensure_ascii=False, indent=2)
