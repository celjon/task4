from abc import ABC, abstractmethod
from typing import List
from domain.shop.shop import Shop


class ShopPersistence(ABC):
    @abstractmethod
    def save(self, name: str, description: str, count_left: int, create_time: str, update_time: str) -> Shop:
        ...

    @abstractmethod
    def delete(self, name: str) -> Shop:
        ...

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Shop:
        ...

    @abstractmethod
    def list_product(self) -> List[Shop]:
        ...

    @abstractmethod
    def buy(self, product_id: int, amount: int) -> Shop:
        ...

    @abstractmethod
    def get_product_by_name(self, product_name: str) -> Shop:
        ...
