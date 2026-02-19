from AI.State import State
import pygame
from AI.FSM import FSM
from AI.AI_Conditions import AI_Conditions
from Commands.MoveCommand import MoveCommand
from Commands.AttackCommand import Attack_command

class Idle_State(State):
    def __init__(self, obj, opponent):
        super().__init__(obj)
        self._opponent = opponent
        self._obj = obj
        self.move_command = MoveCommand(self._obj, pygame.math.Vector2(-1,0), self._obj._speed)
        self.ranged_attack = Attack_command(self._obj, self._obj.direction, self._obj.game_world.attack_types["ranged_attack"], False)

    def Execute(self, delta_time):
        self.move_command.Execute(True, delta_time)

        distance = self._obj.transform.position[0] - self._opponent.transform.position[0]
        if distance <= 140:
            self._obj.fsm.Set_Condition(AI_Conditions.Attack)
        
        return super().Execute()
    
    def Exit(self):
        return super().Exit()
    
    def Enter(self):
        return super().Enter()

