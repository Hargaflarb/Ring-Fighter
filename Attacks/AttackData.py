from Components import Colider
from Components import Momentum
from Components import SpriteRenderer

class Attack_Data():
    def __init__(self, name, timings, hitbox, position_offset, knockback):
        self.name = name
        self._windup_time = timings[0]
        self._hit_time = timings[1]
        self._cooldown_time = timings[2]
        self._hitbox = hitbox # (Width, Height)
        self.position_offset = position_offset
        self._knockback = knockback
        self._ranged_speed = 300

    @property
    def timings(self):
        return (self._windup_time, self._hit_time, self._cooldown_time)

    @property
    def knockback(self):
        return self._knockback

    def Added_components(self, facing):
        components = []
        components.append(Colider((self._hitbox[0]/2,self._hitbox[1],self._hitbox[0]/2,0), 3))

        if False: #ranged
            components.append(Momentum((self._ranged_speed * facing, 0)))
            components.append(SpriteRenderer("rangedsprite")) # this sprite name is not real, gotta figure out how to get the right sprite

        return components

    def Removed_components(self):
        components = []

        if not False: #not ranged
            components.append("Colider")

        return components