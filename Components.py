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
        self._position+=direction

    def Awake(self,game_world):
        pass
    
    def Start(self):
        pass

    def Update(self,delta_time):
        pass

class SpriteRenderer(Component):
    def __init__(self,sprite_name) ->None:
        super().__init__()
        self._sprite_image=pygame.image.load(f"assets\\{sprite_name}")
        self._sprite=pygame.sprite.Sprite()
        self._sprite.rect=self._sprite_image.get_rect()

    @property
    def sprite_image(self):
        return self._sprite_image
    
    @sprite_image.setter
    def sprite_image(self,value):
        self._sprite_image=value

    def Awake(self,game_world):
        self._game_world=game_world
        self._sprite.rect.topleft=self.gameObject.transform.position
        
    def Start(self):
        pass

    def Update(self,delta_time):
        self._game_world.Screen.blit(self._sprite_image,self._sprite.rect)

#collider

#momentum

#gravity

class Animator(Component):
    def __init__(self,spriterenderer):
        super().__init__()
        self.current_index=0
        self.elapsed_time=0
        #change below to gameobject.getcomponent
        self._spriterenderer=spriterenderer
        self.animations={}
        self.frame_speed=0.1
        self.current_animation=None

    def Awake(self,game_world):
        pass
        
    def Start(self):
        pass

    def Update(self,delta_time):
        #set spriterenderer image
        self._spriterenderer.sprite_image=self.current_animation[self.current_index]
        self.elapsed_time+=delta_time
        #switch to next frame
        if self.elapsed_time>=self.frame_speed:
            self.current_index+=1
            if self.current_index >=len(self.current_animation):
                self.current_index=0
        

    def Add_animation(self,animation_name,*args):
        frames=[]
        for arg in args:
            sprite=pygame.image.load(f"assets\\{arg}")
            frames.append(sprite)
        self.animations[animation_name]=frames
        

    def Play_animation(self,animation_name):
        self.current_animation=self.animations[animation_name]
        