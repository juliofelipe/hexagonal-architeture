import sqlite3

import pytest


@pytest.fixture
def setup_database():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        """CREATE TABLE IF NOT EXISTS products (
        "id" string,
        "name" string,
        "price" float,
        "status" string
    );"""
    )

    yield conn
    conn.close()


@pytest.fixture
def setup_test_data(setup_database):
    conn = setup_database
    sample_data = [
        ("abc", "Product Test", 0, "disabled"),
        ("def", "Product Test 1", 10, "enabled"),
    ]

    conn.executemany("INSERT INTO products VALUES(?, ?, ?, ?)", sample_data)
    yield conn
