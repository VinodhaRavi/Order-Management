from abc import ABC, abstractmethod
from entity.user import User
from entity.product import Product
from typing import List

class IOrderManagementRepository(ABC):

    @abstractmethod
    def create_order(self, user: User, products: List[Product]):
        pass

    @abstractmethod
    def cancel_order(self, user_id: int, order_id: int):
        pass

    @abstractmethod
    def create_product(self, user: User, product: Product):
        pass

    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass

    @abstractmethod
    def get_order_by_user(self, user: User):
        pass
