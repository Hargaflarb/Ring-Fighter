import pygame
from Components import Transform

class GameObject:
    def __init__(self,game_world,position):
        #self.sprite_image=pygame.image.load("assets\\image.png")
        #self.sprite=pygame.sprite.Sprite()
        #self.sprite.rect=self.sprite_image.get_rect()
        self.components={}
        # self.transform=self.Add_component(Transform(position))
        self.Add_component(Transform(position))
        self.game_world=game_world

    @property
    def transform(self):
        return self.transform

    def Add_component(self,component):
        component_name=component.__class__.__name__
        self.components[component_name]=component
        component.gameObject=self
        return component
    
    def Get_component(self, component_name):
        for component in self.components.values():
            if component_name == component.__class__.__name__:
                return component
        return None
    
    def Has_component(self, component_name):
        for component in self.components.values():
            if component_name == component.__class__.__name__:
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