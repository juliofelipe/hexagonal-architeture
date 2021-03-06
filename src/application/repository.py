from abc import ABC, abstractmethod
from typing import Optional, Tuple

from application.domain import Product


class ProductReaderInterface(ABC):
    @abstractmethod
    def get(self, id: str) -> Tuple[Product, Optional[Exception]]:
        pass


class ProductWriterInterface(ABC):
    @abstractmethod
    def save(self, product: Product) -> Tuple[Product, Optional[Exception]]:
        pass


class ProductPersistenceInterface(ProductReaderInterface, ProductWriterInterface):
    pass
