from GameObject import GameObject
from Characters.Character import Character
import Components
from Components import Momentum
from Components import Gravity
from Components import Colider
import pygame


class Enemy(Character):
    def __init__(self, game_world, position, scale, character_name):
        super().__init__(game_world, position, scale, character_name)

        speed = 50
        sr = self.Add_component(Components.SpriteRenderer("temp playercharacter.png"))
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(), sr.sprite_image.get_height())

        input_handler = self.Add_component(Components.Input_Handler(self))

        self.Add_component(Momentum())
        self.Add_component(Gravity())
        self.Add_component(Colider((self._sprite_size[0]/3,self._sprite_size[1],self._sprite_size[0]/3,0), 2))

