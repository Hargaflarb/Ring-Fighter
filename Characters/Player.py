from GameObject import GameObject
import Components
import pygame
from abc import ABC
from Commands.move_command import MoveCommand
from Commands.AttackCommand import Attack_command
from Commands.CrouchCommand import Crouch_command
from Commands.MultiCommand import Multi_command
from Components import Momentum
from Components import Gravity
from Components import Colider


class Player(GameObject):
    def __init__(self, game_world, position, scale):
        super().__init__(game_world, position, scale)

        speed = 250
        self._crouching = False
        self.is_blocking_input = False
        self.is_blocking_movement = False
        sr = self.Add_component(Components.SpriteRenderer("temp playercharacter.png"))
        input_handler = self.Add_component(Components.Input_Handler(self))
        self._screen_size = pygame.math.Vector2(game_world.Screen.get_width(), game_world.screen.get_height())
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(), sr.sprite_image.get_height())
        self.game_world = game_world

        input_handler.Add_Command(pygame.K_d, MoveCommand(self, pygame.math.Vector2(1, 0), speed))
        input_handler.Add_Command(pygame.K_a, MoveCommand(self, pygame.math.Vector2(-1, 0), speed))
        input_handler.Add_Command(pygame.K_c, Crouch_command(self))

        standard_attack = Attack_command(self, self.transform.facing, game_world.attack_types["standard_attack"], False)
        low_attack = Attack_command(self, self.transform.facing, game_world.attack_types["low_attack"], True)
        input_handler.Add_Command(pygame.K_j, Multi_command(low_attack, standard_attack, lambda: self.crouching))
        input_handler.Add_Command(pygame.K_k, Attack_command(self, self.transform.facing, game_world.attack_types["down_attack"], False))
        input_handler.Add_Command(pygame.K_l, Attack_command(self, self.transform.facing, game_world.attack_types["up_attack"], False))

        self.Add_component(Momentum())
        self.Add_component(Gravity())
        self.Add_component(Colider((self._sprite_size[0]/2,self._sprite_size[1],self._sprite_size[0]/2,0), 2))


    @property
    def crouching(self):
        return self._crouching

    def Crouch_toggle(self):
        old_rect = self.Get_component("Colider").rect
        if self._crouching: #stops crouching
            self.Get_component("Colider").rect = (old_rect[0], old_rect[1]*2, old_rect[2], old_rect[3])
            self.is_blocking_movement = False
        else: #starts crouching
            self.Get_component("Colider").rect = (old_rect[0], old_rect[1]/2, old_rect[2], old_rect[3])
            self.is_blocking_movement = True
        self._crouching = not self._crouching
 

