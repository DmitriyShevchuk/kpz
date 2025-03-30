from .tech_factory import TechFactory
from devices.balaxy_devices import BalaxyLaptop, BalaxyNetbook, BalaxyEBook, BalaxySmartphone

class BalaxyFactory(TechFactory):
    def create_laptop(self):
        return BalaxyLaptop()

    def create_netbook(self):
        return BalaxyNetbook()

    def create_ebook(self):
        return BalaxyEBook()

    def create_smartphone(self):
        return BalaxySmartphone()
