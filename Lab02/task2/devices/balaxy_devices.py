from .interfaces import Laptop, Netbook, EBook, Smartphone

class BalaxyLaptop(Laptop):
    def info(self) -> str:
        return "Balaxy Laptop - Galaxy Book"

class BalaxyNetbook(Netbook):
    def info(self) -> str:
        return "Balaxy Netbook - Galaxy Net Lite"

class BalaxyEBook(EBook):
    def info(self) -> str:
        return "Balaxy EBook - Galaxy EReader"

class BalaxySmartphone(Smartphone):
    def info(self) -> str:
        return "Balaxy Smartphone - Galaxy S Ultra"
