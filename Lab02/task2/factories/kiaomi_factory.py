from .tech_factory import TechFactory
from devices.kiaomi_devices import KiaomiLaptop, KiaomiNetbook, KiaomiEBook, KiaomiSmartphone

class KiaomiFactory(TechFactory):
    def create_laptop(self):
        return KiaomiLaptop()

    def create_netbook(self):
        return KiaomiNetbook()

    def create_ebook(self):
        return KiaomiEBook()

    def create_smartphone(self):
        return KiaomiSmartphone()
