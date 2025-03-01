from dataclasses import dataclass

from Lab01.Classes.Money import Money

@dataclass
class Product:
    name: str
    amount: int
    unit: str
    price: Money

    def reduce_price(self, other : Money):
        self.price = self.price - other

    def __str__(self):
        return (f'Product name: {self.name}\n'
                f'Price per one {self.unit}: {self.price}\n'
                f'Amount products: {self.amount} {self.unit}\n')