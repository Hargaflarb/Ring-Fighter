import pygame
from abc import ABC,abstractmethod

class Component(ABC):
    def __init__(self)->None:
        super().__init__()
        self.gameObject=None

    @property
    def gameObject(self):
        return self.gameObject
    
    @gameObject.setter
    def gameObject(self,value):
        self.gameObject=value

    @abstractmethod
    def Awake(self,game_world):
        pass
    @abstractmethod
    def Start(self):
        pass
    @abstractmethod
    def Update(self,delta_time):
        pass

class Transform(Component):
    def __init__(self,position):
        super().__init__()
        self.position=position

    @property
    def position(self):
        return self.position
    
    @position.setter
    def position(self,value):
        self.position=value

    def translate(self,direction):
        self.position+=direction

    def Awake(self,game_world):
        pass
    def Start(self):
        pass
    def Update(self,delta_time):
        pass