from .interfaces import Laptop, Netbook, EBook, Smartphone

class IProneLaptop(Laptop):
    def info(self) -> str:
        return "IProne Laptop - MacBook Air"

class IProneNetbook(Netbook):
    def info(self) -> str:
        return "IProne Netbook - iNet mini"

class IProneEBook(EBook):
    def info(self) -> str:
        return "IProne EBook - iRead"

class IProneSmartphone(Smartphone):
    def info(self) -> str:
        return "IProne Smartphone - iPhone Pro Max"
