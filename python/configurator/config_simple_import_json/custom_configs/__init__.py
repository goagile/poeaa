import os

from python.configurator.config_simple_import_json.base_configs.config import Config

PATH = os.path.join(
    'examples',
    'python',
    'configurator',
    'config_simple_import_json',
    'custom_configs',
    'product.json'
)

Product = Config.load(PATH)
