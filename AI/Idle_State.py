from AI.State import State
import pygame
from AI.FSM import FSM
from AI.AI_Conditions import AI_Conditions

class Idle_State(State):
    def __init__(self, obj, opponent):
        super().__init__(obj)
        self._opponent = opponent
        self._obj = obj

    def Execute(self, delta_time):
        self._obj.Move(pygame.math.Vector2(-1, 0), delta_time)

        distance = self._obj.transform.position[0] - self._opponent.transform.position[0]
        if distance <= 100:
            self._obj.fsm.Set_Condition(AI_Conditions.Attack)
     
        return super().Execute()
    
    def Exit(self):
        return super().Exit()
    
    def Enter(self):
        return super().Enter()

