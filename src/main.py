from os import error
import sqlite3

from adapters.db.persistence_adapter import NewSqLitePersistence
from application.service import NewProductService

conn = sqlite3.connect("sqlite3.db")
conn.execute(
        """CREATE TABLE IF NOT EXISTS products (
        "id" string,
        "name" string,
        "price" float,
        "status" string
    );"""
    )

product_db_adapter = NewSqLitePersistence.get_persistence(conn)
product_service = NewProductService.get_service(product_db_adapter)
product, error = product_service.create(name="Product Exemplo", price=30)

product_service.enable(product)

conn.close()