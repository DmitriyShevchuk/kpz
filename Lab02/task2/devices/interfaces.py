from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def info(self) -> str: pass

class Netbook(ABC):
    @abstractmethod
    def info(self) -> str: pass

class EBook(ABC):
    @abstractmethod
    def info(self) -> str: pass

class Smartphone(ABC):
    @abstractmethod
    def info(self) -> str: pass
