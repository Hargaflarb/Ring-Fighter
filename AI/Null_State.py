from AI.State import State
import pygame
from AI.FSM import FSM
from AI.AI_Conditions import AI_Conditions

class Null_State(State):
    def __init__(self, obj):
        super().__init__(obj)

    def Execute(self):
        return super().Execute()
    
    def Enter(self):
        return super().Enter()
    
    def Exit(self):
        return super().Exit()