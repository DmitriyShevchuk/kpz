from .interfaces import Laptop, Netbook, EBook, Smartphone

class KiaomiLaptop(Laptop):
    def info(self) -> str:
        return "Kiaomi Laptop - Mi Notebook"

class KiaomiNetbook(Netbook):
    def info(self) -> str:
        return "Kiaomi Netbook - Mi Netbook Lite"

class KiaomiEBook(EBook):
    def info(self) -> str:
        return "Kiaomi EBook - Mi Reader"

class KiaomiSmartphone(Smartphone):
    def info(self) -> str:
        return "Kiaomi Smartphone - Redmi Note"
