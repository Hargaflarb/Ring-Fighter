from GameObject import GameObject
from abc import ABC

class Character(GameObject):
    def __init__(self, game_world, position, scale):
        super().__init__(game_world, position, scale)
        self._crouching = False
        self._blocking = False

    @property
    def crouching(self):
        return self._crouching
    
    @property
    def blocking(self):
        return self._blocking
    

    def Crouch_toggle(self):
        old_rect = self.Get_component("Colider").rect
        if self._crouching: #stops crouching
            self.Get_component("Colider").rect = (old_rect[0], old_rect[1]*2, old_rect[2], old_rect[3])
            self.input_filter.remove("crouch")
        else: #starts crouching
            self.Get_component("Colider").rect = (old_rect[0], old_rect[1]/2, old_rect[2], old_rect[3])
            self.input_filter.append("crouch")
        self._crouching = not self._crouching
 

    def Block_toggle(self):
        if self._blocking: #stops blocking
            self.input_filter.remove("block")
        else: #starts blocking
            self.input_filter.append("block")
        self._blocking = not self._blocking

    def Take_knockback(self, knockback, facing):
        # play hit animation
        self.Get_component("Momentum").Give_Momentum(knockback, facing)

