from .product import Product
class Electronics(Product):
    def __init__(self, product_id: int, product_name: str, description: str,
                price: float, quantity_in_stock: int, type_: str,
                brand: str, warranty_period: int):
        super().__init__(product_id, product_name, description, price, quantity_in_stock, type_)
        self.brand = brand
        self.warranty_period = warranty_period

    def get_brand(self):
        return self.brand
    def get_warranty_period(self):
        return self.warranty_period


    def set_brand(self, brand):
        self.brand = brand
    def set_warranty_period(self, warranty_period):
        self.warranty_period = warranty_period
    def __str__(self):
        return (super().__str__() + 
                f", Brand={self.brand}, Warranty={self.warranty_period} months")
