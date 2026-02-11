import pygame
from Components import Transform

class GameObject:
    def __init__(self,game_world,position):
        
        self.components={}
        self.game_world=game_world
        self._transform=self.Add_component(Transform(position))
        

    @property
    def transform(self):
        return self._transform
    
    @transform.setter
    def transform(self,value):
        self._transform=value


    def Add_component(self,component):
        component.gameObject=self
        component_name=component.__class__.__name__
        self.components[component_name]=component
        component.Awake(self.game_world)
        component.Start()
        return component
    
    def Awake(self):
        pass
            
    def Start(self):
        pass

    def Update(self,delta_time):
        #run components
        for component in self.components.values():
            component.Update(delta_time)