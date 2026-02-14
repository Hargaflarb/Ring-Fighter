from GameObject import GameObject
import Components
import pygame
from abc import ABC
from Commands.move_command import MoveCommand
from Commands.AttackCommand import Attack_command
from Components import Momentum
from Components import Gravity
from Components import Colider


class Player(GameObject):
    def __init__(self, game_world, position, scale):
        super().__init__(game_world, position, scale)

        speed = 250
        sr = self.Add_component(Components.SpriteRenderer("temp playercharacter.png"))
        input_handler = self.Add_component(Components.Input_Handler(self))
        self._screen_size = pygame.math.Vector2(game_world.Screen.get_width(), game_world.screen.get_height())
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(), sr.sprite_image.get_height())
        self.game_world = game_world

        input_handler.Add_Command(pygame.K_d, MoveCommand(self, pygame.math.Vector2(1, 0), speed))
        input_handler.Add_Command(pygame.K_a, MoveCommand(self, pygame.math.Vector2(-1, 0), speed))
        input_handler.Add_Command(pygame.K_k, Attack_command(self, self.transform.facing))


        self.Add_component(Momentum())
        self.Add_component(Gravity())
        self.Add_component(Colider((self._sprite_size[0]/2,self._sprite_size[1],self._sprite_size[0]/2,0), 2))




 

