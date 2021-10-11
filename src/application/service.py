from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Tuple

from application.domain import NewProduct, Product
from application.repository import ProductPersistenceInterface

class NewProductService:
    @staticmethod
    def get_service(persistence: ProductPersistenceInterface) -> ProductService:
        return ProductService(persistence)


class ProductServiceInterface(ABC):
    @abstractmethod
    def get(self, id: str) -> Tuple[Product, Optional[Exception]]:
        pass

    @abstractmethod
    def create(self, name: str, price: float) -> Tuple[Product, Optional[Exception]]:
        pass

    @abstractmethod
    def enable(self, product: Product) -> Tuple[Product, Optional[Exception]]:
        pass

    @abstractmethod
    def disable(self, product: Product) -> Tuple[Product, Optional[Exception]]:
        pass


class ProductService(ProductServiceInterface):
    def __init__(self, persistence: ProductPersistenceInterface):
        self.persistence = persistence

    def get(self, id: str) -> Tuple[Optional[Product], Optional[Exception]]:
        product, error = self.persistence.get(id)
        if error is not None:
            return None, error
        return product, None

    def create(self, name: str, price: float) -> Tuple[Product, Optional[Exception]]:
        product = NewProduct.get_product(name, price)
        _, error = product.is_valid()
        if error is not None:
            return None, error

        result, error = self.persistence.save(product)
        if error is not None:
            return None, error
        return result, None

    def enable(self, product: Product) -> Tuple[Product, Optional[Exception]]:
        error = product.enable()
        if error is not None:
            return None, error

        result, error = self.persistence.save(product)
        if error is not None:
            return None, error
        return result, None

    def disable(self, product: Product) -> Tuple[Product, Optional[Exception]]:
        error = product.disable()
        if error is not None:
            return None, error

        result, error = self.persistence.save(product)
        if error is not None:
            return None, error
        return result, None
