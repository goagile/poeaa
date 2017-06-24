from examples.factory.test_9.products import (
    ProductA,
    ProductB,
    EmptyProduct
)


class ProductFactory:

    products = {
        0: ProductA(),
        1: ProductB()
    }

    def make_product(self, param):
        product = self.products.get(param)
        if not product:
            return EmptyProduct()
        return product
