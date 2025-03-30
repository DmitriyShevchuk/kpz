from .tech_factory import TechFactory
from devices.iprone_devices import IProneLaptop, IProneNetbook, IProneEBook, IProneSmartphone

class IProneFactory(TechFactory):
    def create_laptop(self):
        return IProneLaptop()

    def create_netbook(self):
        return IProneNetbook()

    def create_ebook(self):
        return IProneEBook()

    def create_smartphone(self):
        return IProneSmartphone()
