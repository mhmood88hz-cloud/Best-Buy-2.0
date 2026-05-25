class Product:
    def __init__(self, name: str, price: float, quantity: int):
        # Validierung der Eingabewerte
        if not name:
            raise ValueError("Der Produktname darf nicht leer sein.")
        if price < 0:
            raise ValueError("Der Preis darf nicht negativ sein.")
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein.")

        # Instanzvariablen initialisieren
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein.")
        self.quantity = quantity
        # Wenn die Menge 0 erreicht, wird das Produkt automatisch deaktiviert
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Die Kaufmenge muss größer als 0 sein.")
        if quantity > self.quantity:
            raise ValueError(f"Nicht genug Bestand. Es sind nur {self.quantity} Stück verfügbar.")

        # Gesamtpreis berechnen
        total_price = self.price * quantity

        # Bestand aktualisieren (nutzt den Setter, um ggf. zu deaktivieren)
        self.set_quantity(self.quantity - quantity)

        return float(total_price)


# Test-Bereich für deine main-Funktion:
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
