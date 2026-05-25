class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Der Produktname darf nicht leer sein.")
        if price < 0:
            raise ValueError("Der Preis darf nicht negativ sein.")
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Standardmäßig keine Aktion zugewiesen

    # Getter & Setter für Promotions
    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def remove_promotion(self):
        self.promotion = None

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        # Zeigt die Aktion an, falls eine aktiv ist
        promo_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_info}")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Die Kaufmenge muss größer als 0 sein.")
        if quantity > self.quantity:
            raise ValueError(f"Nicht genug Bestand. Es sind nur {self.quantity} Stück verfügbar.")

        # Wenn eine Aktion existiert, berechnet diese den Preis. Sonst der Standardweg.
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return float(total_price)


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)
        self.active = True

    def set_quantity(self, quantity: int):
        pass

    def is_active(self) -> bool:
        return True

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Die Kaufmenge muss größer als 0 sein.")

        # Auch hier Promotion berücksichtigen
        if self.promotion:
            return float(self.promotion.apply_promotion(self, quantity))
        return float(self.price * quantity)

    def show(self):
        promo_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        print(f"{self.name}, Price: {self.price}, Quantity: Unlimited{promo_info}")


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Das maximale Bestelllimit muss größer als 0 sein.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Dieses Produkt kann maximal {self.maximum} Mal pro Bestellung gekauft werden.")
        return super().buy(quantity)

    def show(self):
        promo_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max per order: {self.maximum}{promo_info}")
