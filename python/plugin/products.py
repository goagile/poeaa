class ProductA:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


class ProductB:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
