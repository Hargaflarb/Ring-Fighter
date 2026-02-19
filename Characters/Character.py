from GameObject import GameObject
from abc import ABC
from CharacterSoundPack import Character_sound_pack

class Character(GameObject):
    def __init__(self, game_world, position, scale, direction, character_name):
        super().__init__(game_world, position, scale)
        self.input_filter = []
        self._crouching = False
        self._blocking = False
        self._character_name = character_name
        self._sound_pack = Character_sound_pack(self._character_name)
        self._time_since_action = 0 # used for taunt
        self._taunt_wait_time = 7
        self._direction = direction


    @property
    def crouching(self):
        return self._crouching
    
    @property
    def direction(self):
        return self._direction
    
    @property
    def blocking(self):
        return self._blocking
    
    @property
    def sound_pack(self):
        return self._sound_pack

    def Update(self, delta_time):
        self._time_since_action += delta_time
        if self._time_since_action >= self._taunt_wait_time:
            self._sound_pack.Play_Taunt()
            self._time_since_action = 0

        super().Update(delta_time)

    def Action_notification(self):
        self._time_since_action = 0


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
        # resets taunt-timer
        self._time_since_action = 0

        # play hit sound
        self._sound_pack.Play_Hit()

        # play hit animation
        self.Get_component("Momentum").Give_Momentum(knockback, facing)

    