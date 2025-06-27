from .product import Product

class Clothing(Product):
    def __init__(self, product_id: int, product_name: str, description: str,
                price: float, quantity_in_stock: int, type_: str,
                size: str, color: str):
        super().__init__(product_id, product_name, description, price, quantity_in_stock, type_)
        self.size = size
        self.color = color

    def get_size(self):
        return self.size
    def get_color(self):
        return self.color

    def set_size(self, size):
        self.size = size
    def set_color(self, color):
        self.color = color

    def __str__(self):
        return (super().__str__() +
                f", Size={self.size}, Color={self.color}")
