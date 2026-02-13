import pygame
from abc import ABC,abstractmethod
import math

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

    def __init__(self,position,scale):
        super().__init__()
        self._position=position
        self._scale=scale

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self,value):
        self._position=value

    @property
    def scale(self):
        return self._scale
      
    def translate(self,direction):
        self.position = (self.position[0] + direction[0], self.position[1] + direction[1])

    def Awake(self,game_world):
        pass
    
    def Start(self):
        pass

    def Update(self,delta_time):
        pass

class Input_Handler():
    def __init__(self, player):
        super().__init__()
        self._keybinds = {}
        self._player = player

    @property
    def keybinds(self):
        return self._keybinds
    
    @keybinds.setter
    def keybinds(self, value):
        self._keybinds

    def Add_Command(self, key, command):
        self.keybinds[key] = command

    def Update(self, delta_time):
        keys = pygame.key.get_pressed()
        
        for key in self.keybinds.keys():
            if keys[key]:
                self.keybinds[key].Execute(delta_time)

    def Awake(self,game_world):
        pass
        
    def Start(self):
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
        direction = (self.horizontal_momentum * delta_time, self.vertical_momentum * delta_time)
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
        self._size = size # (X,Y,W,H) X = left - Xpos, Y = top - Ypos
        self.hard_colider = False

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,value):
        self._size=value

    @property
    def rect(self):
            pos = self.gameObject.Get_component("Transform").position
            return ((pos[0] + self.size[0]), (pos[1] + self.size[1]), (pos[0] + self.size[2]), (pos[1] + self.size[3]))
            


    def Check_collision(self, other_colider):
        l1, b1, r1, t1 = self.rect
        l2, b2, r2, t2 = other_colider.rect
        return ((l1 < r2) & (r1 > l2)) & ((b1 < t2) & (t1 > b2))

    def Check_Touch(self, other_colider):
        l1, b1, r1, t1 = self.rect
        l2, b2, r2, t2 = other_colider.rect
        return ((l1 <= r2) & (r1 >= l2)) & ((b1 <= t2) & (t1 >= b2))

    def Overlap(self, other_colider):
        l1, b1, r1, t1 = self.rect
        l2, b2, r2, t2 = other_colider.rect
        return (max(l1,l2), max(b1,b2), min(r1, r2), min(t1, t2))


    def On_collision(self, other_colider):
        if self.hard_colider:
            return
        if other_colider.hard_colider: # if only the other is a hard colider
            # hard colider
            print("hard collision")
            overlap = self.Overlap(other_colider)

            overlap_width = overlap[2] - overlap[0]
            overlap_height = overlap[3] - overlap[1]

            if overlap_width >= overlap_height:
                pos = (0.0, overlap_height)
                self.gameObject.Get_component("Momentum").vertical_momentum = 0
            else:
                pos = (overlap_width, 0.0)
                self.gameObject.Get_component("Momentum").horizontal_momentum = 0

            self.gameObject.Get_component("Transform").translate(pos)

        else: # if neither are hard coliders
            # custom collision
            self.gameObject.OnCollision(other_colider.gameObject)        


    def Awake(self,game_world):
        # hard-collisions are only done for objects with Momentum.
        self.hard_colider = not self.gameObject.Has_component("Momentum")

    def Start(self):
        pass
    def Update(self, delta_time):
        pass

class SpriteRenderer(Component):
    def __init__(self,sprite_name) ->None:
        super().__init__()
        #!make sure the asset is in the correct sub-folder!
        self._sprite_image=pygame.image.load(f"assets\\Images\\{sprite_name}")
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
        self.sprite_image=pygame.transform.scale(self.sprite_image,(self.gameObject.transform.scale*self.sprite_image.width,(self.gameObject.transform.scale*self.sprite_image.height)))
        self._sprite.rect.topleft=self.gameObject.transform.position
        
        
    def Start(self):
        pass

    def Update(self,delta_time):
        self._sprite.rect.topleft=self.gameObject.transform.position
        self._game_world.Screen.blit(self._sprite_image,self._sprite.rect)


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
            #!make sure the asset is in the correct sub-folder!
            sprite=pygame.image.load(f"assets\\Images\\{arg}")
            frames.append(sprite)
        self.animations[animation_name]=frames
        

    def Play_animation(self,animation_name):
        self.current_animation=self.animations[animation_name]
        
