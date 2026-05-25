from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """Berechnet den Gesamtpreis für eine bestimmte Menge nach Abzug des Rabatts."""
        pass


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return float(total_price - discount)


class SecondHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        # Wie viele Paare gibt es? (Jeder 2. Artikel ist zum halben Preis)
        pairs = quantity // 2
        remainder = quantity % 2

        # Preis berechnen: Vollpreis für den ersten + halber Preis für den zweiten eines Paars
        price_per_pair = product.price + (product.price * 0.5)
        total = (pairs * price_per_pair) + (remainder * product.price)
        return float(total)


class ThirdOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        # Gruppen von 3 Artikeln (Zwei bezahlen, einer gratis)
        triplets = quantity // 3
        remainder = quantity % 3

        # Man bezahlt 2 von 3 Artikeln pro Gruppe
        payable_quantity = (triplets * 2) + remainder
        return float(payable_quantity * product.price)
