from GameObject import GameObject
from abc import ABC

class Character(GameObject):

    def __init__(self):
        super.__init__()
        # self._crouching = False

        
    # def Crouch_toggle(self):
    #     old_rect = self.Get_component("Colider").rect
    #     if self._crouching:
    #         self.Get_component("Colider").rect = (old_rect[0], old_rect[1]/2, old_rect[2], old_rect[3])
    #     else:
    #         self.Get_component("Colider").rect = (old_rect[0], old_rect[1]*2, old_rect[2], old_rect[3])
    #     self._crouching = not self._crouching
    #     #stop movement here
