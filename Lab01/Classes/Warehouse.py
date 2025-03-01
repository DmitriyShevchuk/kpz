from dataclasses import dataclass, field
from datetime import datetime

from Lab01.Classes.Money import Money
from Lab01.Classes.Product import Product
from Lab01.Classes.Reporting import Reporting

@dataclass
class Warehouse:
    last_delivery : datetime = datetime.now().__format__('%d.%m.%Y %H:%M')
    first_delivery : datetime = datetime.now().__format__('%d.%m.%Y %H:%M')
    products : list[Product] = field(default_factory=list)

    def append_product(self, other: list):
        self.products = self.products + other
        self.update_last_delivery()
        Reporting.create_invoice('Expense invoice', other, self.last_delivery)

    def remove_product(self, name : str, amount : int):
        for product in self.products:
            if product.name == name:
                product.amount -= amount

                receipt_product = product
                receipt_product.amount = amount
                Reporting.create_invoice('Receipt invoice', [receipt_product], self.last_delivery)
                return
        else:
            print('Product not found')

    def inventory(self):
        Reporting.create_invoice('Inventory report', self.products, self.last_delivery)

    def update_last_delivery(self):
        self.last_delivery = datetime.now().__format__('%d.%m.%Y %H:%M')

    def __str__(self):
        return (f'{'\n'.join([str(product) for product in self.products])}\n'
                f'Date of last delivery: {self.last_delivery}')
