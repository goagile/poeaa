import os
import json

PATH = os.path.join(
    'examples',
    'python',
    'simple_import_json',
    'product.json'
)


def load(path):
    print('Try to import')
    result = {}
    with open(path, 'r') as file:
        result = json.load(file)
    return result


product = load(PATH)
