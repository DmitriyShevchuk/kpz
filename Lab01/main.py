from Classes.Money import Money
from Classes.Product import Product
from datetime import datetime

from Lab01.Classes.Warehouse import Warehouse
from Lab01.Classes.Reporting import Reporting


def main():
    product1 = Product(
        name='Apple',
        amount=100,
        unit='kg',
        price=Money(5, 50, currency='euro')
    )

    product2 = Product(
        name='Mango',
        amount=50,
        unit='kg',
        price=Money(7, 25, currency='dollar')
    )

    product3 = Product(
        name='Iphone 16 Pro Max',
        amount=5,
        unit='item',
        price=Money(1300, currency='dollar')
    )

    warehouse = Warehouse(
        products=[
            product1,
            product2
        ]
    )

    warehouse.append_product(
        other = [
            product3
        ]
    )

    warehouse.remove_product('Iphone 16 Pro Max', 1)

    warehouse.update_last_delivery()


if __name__ == '__main__':
    main()