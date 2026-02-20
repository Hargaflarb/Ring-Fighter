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

    def __init__(self,position,scale, facing = 1):
        super().__init__()
        self._position=position
        self._scale=scale
        self.facing = facing

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
        self._last_keypresses = []
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
                self.keybinds[key].Execute(self._last_keypresses[key], delta_time)
        
        self._last_keypresses = keys

    def Awake(self,game_world):
        self._last_keypresses = pygame.key.get_pressed()
        
    def Start(self):
        pass


class Gravity(Component):

    def __init__(self):
        super().__init__()
        self.last_delta_time = 0
        self._gravity = 9.82
        self._gravity_multiplier = 50
        
    @property
    def gravity(self):
        return self._gravity * self._gravity_multiplier

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
    def __init__(self, momentum = (0.0,0.0)):
        super().__init__()
        self._horizontal_momentum = momentum[0]
        self._vertical_momentum = momentum[1]

    @property
    def horizontal_momentum(self):
        return self._horizontal_momentum
    @horizontal_momentum.setter
    def horizontal_momentum(self, value):
        if abs(value) < 1:
            value = 0
        self._horizontal_momentum = value
    
    @property
    def vertical_momentum(self):
        return self._vertical_momentum
    @vertical_momentum.setter
    def vertical_momentum(self, value):
        self._vertical_momentum = value


    def Awake(self,game_world):
        pass
    def Start(self):
        pass

    def Update(self, delta_time):
        transform = self.gameObject.Get_component("Transform")# Transform() # get the transform
        direction = (self.horizontal_momentum * delta_time, self.vertical_momentum * delta_time)
        transform.translate(direction)
        # print(f"momentum: {self.horizontal_momentum} | {self.vertical_momentum}")
        # print(f"position: {transform.position}\n")
        return super().Update(delta_time)
    

    def Give_Momentum(self, knockback, facing):
        self.horizontal_momentum -= knockback[0] * facing
        self.vertical_momentum -= knockback[1]

    
    
class Colider(Component):
    def __init__(self, rect, colider_type):
        super().__init__()
        # (L,T,R,B) L = left dist, T = top dist, R = right dist, B = bottom dist
        self._rect = rect
        self.colider_type = colider_type
        # 1 = Hard colider; can't be pushed, but pushes soft coliders
        # 2 = Soft colider; is pushed by hard coliders, but can't push itself
        # 3 = Transparent colider; can't be pushed and does not push itself

    # def __init__(self, size, colider_type):
    #     super().__init__()
    #     # (W,H) W = width, H = height
    #     self._rect = (size[0]/2,size[1],size[0]/2,0)
    #     self.colider_type = colider_type
    #     # 1 = Hard colider; can't be pushed, but pushes soft coliders
    #     # 2 = Soft colider; is pushed by hard coliders, but can't push itself
    #     # 3 = Transparent colider; can't be pushed and does not push itself


    @property
    def rect(self):
        return self._rect
    
    @rect.setter
    def rect(self,value):
        self._rect=value

    @property
    def pos_rect(self):
            pos = self.gameObject.transform.position
            return ((pos[0] - self.rect[0]), (pos[1] - self.rect[1]), (pos[0] + self.rect[2]), (pos[1] + self.rect[3]))
    
    @property
    def pos_sized_rect(self):
            pos = self.gameObject.transform.position
            return ((pos[0] - self.rect[0]), (pos[1] - self.rect[1]), (self.rect[0] + self.rect[2]), (self.rect[1] + self.rect[3]))
            


    def Check_collision(self, other_colider):
        l1, t1, r1, b1 = self.pos_rect
        l2, t2, r2, b2 = other_colider.pos_rect
        #print(f"{(l1 < r2)} | {(r1 > l2)} | {(t1 < b2)} | {(b1 > t2)}")
        return ((l1 < r2) & (r1 > l2)) & ((t1 < b2) & (b1 > t2))

    def Check_Touch(self, other_colider):
        l1, t1, r1, b1 = self.pos_rect
        l2, t2, r2, b2 = other_colider.pos_rect
        return ((l1 <= r2) & (r1 >= l2)) & ((t1 <= b2) & (b1 >= t2))

    def Overlap(self, other_colider):
        l1, t1, r1, b1 = self.pos_rect
        l2, t2, r2, b2 = other_colider.pos_rect
        # print(f"{(self.Lower_absolute_value(r2 - l1, l2 - r1), self.Lower_absolute_value(t2 - b1, b2 - t1))}")
        return (self.Lower_absolute_value(r2 - l1, l2 - r1), self.Lower_absolute_value(t2 - b1, b2 - t1))

    def Lower_absolute_value(self, value1, value2):
        if abs(value1) < abs(value2):
            return value1
        return value2
    

    def On_collision(self, other_colider):
        if (self.colider_type == 2) & (other_colider.colider_type == 1): # hard collision
            #print("hard collision")
            if self.Check_collision(other_colider):
                overlap = self.Overlap(other_colider)

                overlap_width = overlap[0]
                overlap_height = overlap[1]

                if abs(overlap_width) >= abs(overlap_height):
                    pos = (0.0, overlap_height)
                    self.gameObject.Get_component("Momentum").vertical_momentum = 0
                else:
                    pos = (overlap_width, 0.0)
                    self.gameObject.Get_component("Momentum").horizontal_momentum = 0
                    
                self.gameObject.transform.translate(pos)
            else:
                self.gameObject.Get_component("Momentum").horizontal_momentum *= 0.8


        # custom collision
        self.gameObject.OnCollision(other_colider.gameObject)        


    def Awake(self,game_world):
        self._game_world = game_world
    def Start(self):
        pass
    def Update(self, delta_time):
        pass
        # draw hitboxes
        # pygame.draw.rect(self._game_world.Screen, pygame.color.Color(255,0,0), pygame.rect.Rect(self.pos_sized_rect), 1)
        # pygame.draw.circle(self._game_world.Screen, pygame.color.Color(255,0,0), self.gameObject.transform.position, 1, 0)


class SpriteRenderer(Component):
    def __init__(self,sprite_name) ->None:
        super().__init__()
        #!make sure the asset is in the correct sub-folder!
        self._sprite_image=pygame.image.load(f"assets\\Images\\{sprite_name}")
        #self._sprite_image = self.Flip(self._sprite_image, direction)
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
        self._sprite.rect.topleft = self.Apply_sprite_offset(self.gameObject.transform.position)
        flipped_sprite = self.Flip(self._sprite_image, self.gameObject.transform.facing)
        self._game_world.Screen.blit(flipped_sprite,self._sprite.rect)

    def Apply_sprite_offset(self, position):
        x = position[0] - (self.sprite_image.get_width()/2)
        y = position[1] - (self.sprite_image.height)
        return pygame.math.Vector2(x,y)
    
      
    def Flip(self, sprite, direction):
        if direction == -1:
            flipped_image = pygame.transform.flip(sprite, True, False)  
        elif direction == 1:
            flipped_image = pygame.transform.flip(sprite, False, False)
        else:
            flipped_image = sprite
        return flipped_image
        



class Animator(Component):
    def __init__(self, spriterenderer):
        super().__init__()
        self.current_index=0
        self.elapsed_time=0
        #change below to gameobject.getcomponent
        self._spriterenderer=spriterenderer
        self.animations={}
        self.default_animation = None
        self.frame_speed=0.1
        self.current_animation=None
        self._loop_current = True

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
            self.elapsed_time -= self.frame_speed
            if (self.current_index >= len(self.current_animation)):
                if (self._loop_current):
                    self.current_index=0
                else:
                    self.Stop_animation()
        

    def Add_animation(self,animation_name, args):
        frames=[]
        for arg in args:
            #!make sure the asset is in the correct sub-folder!
            sprite=pygame.image.load(f"assets\\Images\\{arg}")
            frames.append(sprite)
        self.animations[animation_name]=frames
        
    def Set_default_animation(self, animation_name):
        self.default_animation = self.animations[animation_name]


    def Play_animation(self,animation_name, do_loop):
        self.current_index = 0
        self._loop_current = do_loop
        self.current_animation=self.animations[animation_name]
  
    def Stop_animation(self):
        self.current_index = 0
        self._loop_current = True
        self.current_animation=self.default_animation
