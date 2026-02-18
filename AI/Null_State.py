from AI.State import State
import pygame
from AI.FSM import FSM
from AI.AI_Conditions import AI_Conditions

class Null_State(State):
    def __init__(self, obj, opponent):
        super().__init__(obj)
        self._opponent = opponent
        self._obj = obj

    def Execute(self, delta_time):
        self._obj.fsm.Set_Condition(AI_Conditions.Idle)
        return super().Execute()
    
    def Enter(self):
        return super().Enter()
    
    def Exit(self):
        return super().Exit()