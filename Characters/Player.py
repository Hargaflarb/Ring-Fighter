from GameObject import GameObject
from Characters.Character import Character
import Components
import pygame
from abc import ABC
from Commands.MoveCommand import MoveCommand
from Commands.AttackCommand import Attack_command
from Commands.CrouchCommand import Crouch_command
from Commands.BlockCommand import Block_command
from Commands.MultiCommand import Multi_command
from Components import Momentum
from Components import Gravity
from Components import Colider
from Components import Input_Handler


class Player(Character):
    def __init__(self, game_world, position, scale, direction, character_name, difficulty):
        super().__init__(game_world, position, scale, direction, character_name, difficulty)
        input_handler = self.Add_component(Input_Handler(self))
        self._screen_size = pygame.math.Vector2(game_world.Screen.get_width(), game_world.screen.get_height())
        self.game_world = game_world
        
        # movement
        speed = 250
        input_handler.Add_Command(pygame.K_d, MoveCommand(self, pygame.math.Vector2(1, 0), speed))
        input_handler.Add_Command(pygame.K_a, MoveCommand(self, pygame.math.Vector2(-1, 0), speed))

        # other
        input_handler.Add_Command(pygame.K_s, Crouch_command(self))
        input_handler.Add_Command(pygame.K_SPACE, Block_command(self))
        
        # attacks
        standard_attack = Attack_command(self, self.transform.facing, self.attack_types["standard_attack"], False)
        low_attack = Attack_command(self, self.transform.facing, self.attack_types["low_attack"], True)
        input_handler.Add_Command(pygame.K_j, Multi_command(low_attack, standard_attack, lambda: self.crouching))
        input_handler.Add_Command(pygame.K_k, Attack_command(self, self.transform.facing, self.attack_types["down_attack"], False))
        # input_handler.Add_Command(pygame.K_l, Attack_command(self, self.transform.facing, game_world.attack_types["up_attack"], False))
        input_handler.Add_Command(pygame.K_h, Attack_command(self, self.transform.facing, self.attack_types["ranged_attack"], False))

        self.Add_component(Momentum())
        self.Add_component(Gravity())
        self.Add_component(Colider((self._sprite_size[0]/3,self._sprite_size[1],self._sprite_size[0]/3,0), 2))



