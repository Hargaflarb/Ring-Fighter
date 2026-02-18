from abc import ABC
from abc import abstractmethod

class State(ABC):
    def __init__(self, obj):
        pass

    @abstractmethod
    def Enter(self):
        pass

    @abstractmethod
    def Execute(self):
        pass

    @abstractmethod
    def Exit(self):
        pass