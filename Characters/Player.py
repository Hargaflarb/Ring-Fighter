from GameObject import GameObject
import Components
import pygame
from abc import ABC
from Commands.move_command import MoveCommand


class Player(GameObject):
    def __init__(self, game_world, position, scale):
        super().__init__(game_world, position, scale)

        speed = 50
        sr = self.Add_component(Components.SpriteRenderer("temp playercharacter.png"))
        input_handler = self.Add_component(Components.Input_Handler(self))
        self._screen_size = pygame.math.Vector2(game_world.Screen.get_width(), game_world.screen.get_height())
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(), sr.sprite_image.get_height())
        self.transform.position.x -= (self._sprite_size.x/2)
        self.transform.position.y -= (self._sprite_size.y/2)
        self.game_world = game_world

        input_handler.Add_Command(pygame.K_d, MoveCommand(self, pygame.math.Vector2(1, 0), speed))
        input_handler.Add_Command(pygame.K_a, MoveCommand(self, pygame.math.Vector2(-1, 0), speed))



 

