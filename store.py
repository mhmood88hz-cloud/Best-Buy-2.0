from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products: List[Product] = None):
        # Wenn keine Produktliste übergeben wird, starten wir mit einer leeren Liste
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product: Product):
        # Fügt ein neues Produkt zur Liste des Stores hinzu
        self.products.append(product)

    def remove_product(self, product: Product):
        # Entfernt ein Produkt aus dem Store, falls es existiert
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        # Rechnet die Mengen aller Produkte im Store zusammen
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[Product]:
        # Gibt eine Liste zurück, die NUR aktive Produkte enthält
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        # Verarbeitet eine Liste von Bestellungen (Produkt, Menge)
        total_price = 0.0

        for product, quantity in shopping_list:
            # Nutzt die buy()-Methode des Produkts, um den Preis zu berechnen
            # und das Produkt zieht die Menge automatisch von seinem Lagerbestand ab
            total_price += product.buy(quantity)

        return total_price


# Test-Bereich für deine main-Funktion:
if __name__ == "__main__":
    import products  # Temporärer Import für die manuelle Testliste unten

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))
