import pygame
from abc import ABC,abstractmethod

class Component(ABC):
    def __init__(self)->None:
        super().__init__()
        self._gameObject=None

    @property
    def gameObject(self):
        return self._gameObject
    
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
        self._position=position

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self,value):
        self._position=value

    def translate(self,direction):
        self.position = (self.position[0] + direction[0], self.position[1] + direction[1])

    def Awake(self,game_world):
        pass
    def Start(self):
        pass
    def Update(self,delta_time):
        pass


class Gravity(Component):

    def __init__(self):
        super().__init__()
        self.last_delta_time = 0
        self.gravity = -9.82
        
    def Awake(self,game_world):
        pass
    def Start(self):
        pass

    def Update(self, delta_time):
        momentum = self.gameObject.Get_component("Momentum") #get the momentum
        momentum.vertical_momentum += self.gravity * (self.last_delta_time / 2)
        momentum.vertical_momentum += self.gravity * (delta_time / 2)
        self.last_delta_time = delta_time
        return super().Update(delta_time)


class Momentum(Component):
    def __init__(self):
        super().__init__()
        self.vertical_momentum = 0.0
        self.horizontal_momentum = 0.0

    def Awake(self,game_world):
        pass
    def Start(self):
        pass

    def Update(self, delta_time):
        transform = self.gameObject.Get_component("Transform")# Transform() # get the transform
        direction = (self.vertical_momentum * delta_time, self.horizontal_momentum * delta_time)
        transform.translate(direction)
        print(f"momentum: {self.horizontal_momentum} | {self.vertical_momentum}")
        print(f"position: {transform.position}\n")
        return super().Update(delta_time)
    

    def Give_Momentum(self):
        self.vertical_momentum = 1
        self.horizontal_momentum = 1

    
    
class Colider(Component):
    def __init__(self, size):
        super().__init__()
        self._size = size
        # hard-collisions are only done for objects with Momentum.
        self.hard_colider = not self.gameObject.Has_component("Momentum")

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,value):
        self._size=value


    def Check_collision(self, other_colider):
        if self.hard_colider:
            return
        if other_colider.hard_colider: # if only the other is a hard colider
            # hard-collision
            self.gameObject.Get_component("Momentum").vertical_momentum = 0
            print("hard collision")
        else: # if neither are hard coliders
            # custom collision
            self.gameObject.OnCollision(other_colider.gameObject)


    def Awake(self,game_world):
        pass
    def Start(self):
        pass
    def Update(self, delta_time):
        pass