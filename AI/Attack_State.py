from AI.State import State
from AI.AI_Conditions import AI_Conditions
import random
from Commands.AttackCommand import Attack_command
from Commands.MoveCommand import MoveCommand
from Commands.CrouchCommand import Crouch_command
from Commands.BlockCommand import Block_command
import pygame
import time

class Attack_State(State):
    def __init__(self, obj, opponent):
        super().__init__(obj)
        self._opponent = opponent
        self._obj = obj
        self.move_command = MoveCommand(self._obj, pygame.math.Vector2(-1,0), self._obj._speed)
        self.crouch_command = Crouch_command(self._obj)

        self.standard_attack = Attack_command(self._obj, self._obj.direction, self._obj.game_world.attack_types["standard_attack"], False)
        self.down_attack = Attack_command(self._obj, self._obj.direction, self._obj.game_world.attack_types["down_attack"], False)
        self.up_attack = Attack_command(self._obj, self._obj.direction, self._obj.game_world.attack_types["up_attack"], False)
        self.low_attack = Attack_command(self._obj, self._obj.direction, self._obj.game_world.attack_types["low_attack"], True)
        self.ranged_attack = Attack_command(self._obj, self._obj.direction, self._obj.game_world.attack_types["ranged_attack"], False)
        self.block_command = Block_command(self._obj)
        self.countdown = 0

    def Execute(self, delta_time):
        distance = self._obj.transform.position[0] - self._opponent.transform.position[0]
        
        self.countdown += delta_time


        if self._obj.blocking == False and "attack" not in self._obj.input_filter and "attack" in self._opponent.input_filter:
                self.block_command.Execute(False, self._obj.game_world.delta_time)
                self.countdown = 0
        else:
            if self._opponent.crouching == True:
                self.move_command.Execute(True, self._obj.game_world.delta_time)
                if distance <= 100:
                    self.down_attack.Execute(False, self._obj.game_world.delta_time)
            elif self._opponent.blocking == True and self._obj.crouching == False:
                if distance >= 100:
                    self.move_command.Execute(True, self._obj.game_world.delta_time)
                else:
                    self.crouch_command.Execute(False, self._obj.game_world.delta_time)
            elif self._opponent.blocking == True and self._obj.crouching == True:
                if distance <= 100: 
                    self.low_attack.Execute(False, self._obj.game_world.delta_time)
                else:
                    self.crouch_command.Execute(False, self._obj.game_world.delta_time)
            elif self._opponent.blocking == False and self._obj.crouching == True:
                self.crouch_command.Execute(False, self._obj.game_world.delta_time)
            elif self._obj.blocking == True and self.countdown >= 0.5:
                self.block_command.Execute(False, self._obj.game_world.delta_time)
            else:
                self.standard_attack.Execute(False, self._obj.game_world.delta_time)

        if distance >= 140:
            self._obj.fsm.Set_Condition(AI_Conditions.Idle)

        return super().Execute()
    
    def Enter(self):
        return super().Enter()
    
    def Exit(self):
        return super().Exit()