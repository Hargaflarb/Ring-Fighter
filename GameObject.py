import pygame
from Components import Transform

class GameObject:
    def __init__(self,game_world,position,scale):
        self.components={}
        self.game_world=game_world
        self._transform=self.Add_component(Transform(position,scale))

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
    
    def Remove_all_components(self):
        self.components.clear()

    def Remove_component(self, component_name):
        if component_name in self.components.keys():
            del self.components[component_name]

    def Get_component(self, component_name):
        if component_name in self.components.keys():
            return self.components[component_name]
        return None
    
    def Has_component(self, component_name):
        if component_name in self.components.keys():
            return True
        return False

    
    def Awake(self):
        for component in self.components.values():
            component.Awake(self.game_world)
            
    def Start(self):
        for component in self.components.values():
            component.Start()
    
    def Update(self,delta_time):
        #run components
        for component in self.components.values():
            component.Update(delta_time)
        #self.game_world.Screen.blit(self.sprite_image,self.sprite.rect)
        pass

    def OnCollision(self, other):
        pass
