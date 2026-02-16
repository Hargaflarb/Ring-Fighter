from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def blocking_filters(self):
        pass

    @abstractmethod
    def Execute(self, is_repeated):
        pass

    
    def Pass_filter(self, filters):
        for filter in filters:
            if filter in self.blocking_filters:
                return False
        return True
