<details>
<summary>Lab01</summary>

## 1. Object-Oriented Programming (OOP)
Classes and Objects: Money, Product, and Warehouse are implemented as classes with attributes and methods.
File: [Lab01/Classes/Money.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Money.py), [Lab01/Classes/Product.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Product.py), [Lab01/Classes/Warehouse.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Warehouse.py)

Encapsulation: Attributes like price in Product and products in Warehouse are accessed via methods.
[File: Lab01/Classes/Product.py, Method: reduce_price](https://github.com/DmitriyShevchuk/kpz/blob/main/Lab01/Classes/Product.py#L12)


## 2. Abstraction
Simplifying Interactions: Methods in Product and Warehouse abstract complex operations like reducing prices and managing inventory.
File: [Lab01/Classes/Product.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Product.py), [Lab01/Classes/Warehouse.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Warehouse.py)

## 3. Composition
Product contains Money, and Warehouse contains a list of Product objects.
File: [Lab01/Classes/Warehouse.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Warehouse.py)

## 4. Error Handling
Money raises exceptions for invalid operations like subtracting negative amounts or mismatched currencies.
File: [Lab01/Classes/Money.py, Method: __sub_errors](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Money.py#L12)

## 5. Separation of Concerns
Each class has a clear responsibility (e.g., Product for product data, Reporting for reports).
File: [Lab01/Classes/Product.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Product.py), [Lab01/Classes/Reporting.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Reporting.py)

## 6. Modularity
The code is split into independent modules, making it easy to maintain and extend.
File: [Lab01/Classes/Money.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Money.py), [Lab01/Classes/Reporting.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Reporting.py)

## 7. DRY (Don’t Repeat Yourself)
The __str__ method in Money and Product avoids repeating string formatting logic.
File: [Lab01/Classes/Money.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Money.py), [Lab01/Classes/Product.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Product.py)

## 8. Single Responsibility Principle (SRP)
Each class has a single responsibility, such as handling money or managing products.
File: [Lab01/Classes/Money.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Money.py), [Lab01/Classes/Product.py](https://github.com/DmitriyShevchuk/kpz/blob/70a582f1c037ffb70c56d30532c4a335f19626a0/Lab01/Classes/Product.py)

</details>
