from Components import Colider
from Components import Momentum
from Components import SpriteRenderer
from Attacks.RangedAttack import Ranged_attack
from Attacks.Attack import Attack

class Attack_Data():
    def __init__(self, name, timings, hitbox, position_offset, knockback, ignores_block):
        self.name = name
        self._windup_time = timings[0]
        self._hit_time = timings[1]
        self._cooldown_time = timings[2]
        self._hitbox = hitbox # (Width, Height)
        self.position_offset = position_offset
        self._knockback = knockback
        self._ignores_block = ignores_block
        self._ranged_speed = -300

    @property
    def timings(self):
        return (self._windup_time, self._hit_time, self._cooldown_time)

    @property
    def knockback(self):
        return self._knockback
    
    @property
    def ignores_block(self):
        return self._ignores_block

    def Make_attack_object(self, game_world, character):
        if self.name == "ranged_attack":
            return Ranged_attack(game_world, character, self)
        else:
            return Attack(game_world, character, self)


    def Added_components(self, facing):
        components = []
        components.append(Colider((self._hitbox[0]/2,self._hitbox[1],self._hitbox[0]/2,0), 3))

        if self.name == "ranged_attack":
            components.append(Momentum((self._ranged_speed * facing, 0)))
            # components.append(SpriteRenderer("rangedsprite")) # this sprite name is not real, gotta figure out how to get the right sprite

        return components

    def Removed_components(self):
        components = []

        if self.name != "ranged_attack": # this if-statement isn't really needed
            components.append("Colider")

        return components