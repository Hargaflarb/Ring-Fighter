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
        self._gameObject=value

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
        self._position=value

    def translate(self,direction):
        self.position+=direction

    def Awake(self,game_world):
        pass
    
    def Start(self):
        pass

    def Update(self,delta_time):
        pass

class SpriteRenderer(Component):
    def __init__(self,sprite_name) ->None:
        super().__init__()
        self.sprite_image=pygame.image.load(f"assets\\{sprite_name}")
        self.sprite=pygame.sprite.Sprite()
        self.sprite.rect=self.sprite_image.get_rect()

    def Awake(self,game_world):
        self.game_world=game_world
        
    def Start(self):
        pass

    def Update(self,delta_time):
        self.game_world.Screen.blit(self.sprite_image,self.sprite.rect)

#collider

#momentum

#gravity

#animator