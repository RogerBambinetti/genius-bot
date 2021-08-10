from abc import ABC, abstractmethod

class AbstractDao(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def database(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def list(self):
        pass