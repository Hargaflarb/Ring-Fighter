from AI.State import State
import pygame

class Idle_State(State):
    def __init__(self, obj, opponent):
        super().__init__(obj)
        self._opponent = opponent
        self._obj = obj

    def Execute(self):
        self.obj.Move(pygame.math.Vector2(-1, 0))

        distance = self._obj.transform.position.x - self._opponent.transform.position.x
     
        return super().Execute()
    
    def Exit(self):
        return super().Exit()
    
    def Enter(self):
        print("Idle")
        return super().Enter()

