from abc import ABC, abstractmethod
from devices.interfaces import Laptop, Netbook, EBook, Smartphone

class TechFactory(ABC):
    @abstractmethod
    def create_laptop(self) -> Laptop: pass

    @abstractmethod
    def create_netbook(self) -> Netbook: pass

    @abstractmethod
    def create_ebook(self) -> EBook: pass

    @abstractmethod
    def create_smartphone(self) -> Smartphone: pass
