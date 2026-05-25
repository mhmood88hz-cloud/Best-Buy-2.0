import pytest
from products import Product


def test_creating_prod():
    # Test, dass das Erstellen eines normalen Produkts funktioniert
    prod = Product("MacBook Air M2", price=1450, quantity=100)
    assert prod.name == "MacBook Air M2"
    assert prod.price == 1450
    assert prod.get_quantity() == 100
    assert prod.is_active() is True


def test_creating_prod_invalid_details():
    # Test, dass ungültige Details Ausnahmen (Exceptions) auslösen
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_prod_becomes_inactive():
    # Test, dass ein Produkt bei Menge 0 inaktiv wird
    prod = Product("MacBook Air M2", price=1450, quantity=1)
    prod.buy(1)
    assert prod.get_quantity() == 0
    assert prod.is_active() is False


def test_buy_modifies_quantity():
    # Test, dass der Kauf die Menge ändert und den richtigen Preis zurückgibt
    prod = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = prod.buy(10)
    assert total_price == 14500.0
    assert prod.get_quantity() == 90


def test_buy_too_much():
    # Test, dass der Kauf einer zu großen Menge eine Ausnahme auslöst
    prod = Product("MacBook Air M2", price=1450, quantity=10)
    with pytest.raises(ValueError):
        prod.buy(11)
