from examples.python.config.config import Config, Field


class Products(Config):
    Velo = Field(label='Велотренажер')
    Aqua = Field(label='Водный мотоцикл')
