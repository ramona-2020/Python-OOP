from project.product import Product


class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.grams = grams


    def grams(self):
        return self.grams
