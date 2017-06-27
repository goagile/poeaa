import json
import unittest

PATH = 'examples/python/json_builder/products.json'


class TestJSONBuilder(unittest.TestCase):

    def make(self):
        return JsonBuilder()

    def test_add_product(self):
        expected = {
            'Product': []
        }
        builder = self.make()
        builder.add_product('Product')

        result = builder.items

        self.assertEqual(expected, result)

    def test_add_field_param(self):
        expected = {
            'Product': [{
                'name': 'Kg',
                'label': 'Килограмм'
            }]
        }
        builder = self.make()
        builder.add_product('Product')
        builder.add_field(name='Kg', label='Килограмм')

        result = builder.items

        self.assertEqual(expected, result)

    def test_json_builder(self):
        expected = {
            'Product': [{
                'name': 'Kg',
                'label': 'Килограмм'
            }]
        }
        builder = self.make()
        builder.add_product('Product')
        builder.add_field(name='Kg', label='Килограмм')
        builder.save(path=PATH)

        result = self.load(PATH)

        self.assertEqual(expected, result)

    def load(self, path):
        with open(PATH, 'r') as file:
            result = json.load(file)
        return result


class Builder:

    def __init__(self):
        self.name = ''
        self.items = {}

    def add_product(self, name):
        self.name = name
        self.items[self.name] = []

    def add_field(self, **kwargs):
        self.items[self.name].append(kwargs)


class JsonBuilder(Builder):

    def save(self, path):
        with open(path, 'w') as file:
            json.dump(self.items, fp=file, ensure_ascii=False, indent=2)
