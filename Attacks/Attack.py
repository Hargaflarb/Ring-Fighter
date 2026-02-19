from GameObject import GameObject

class Attack(GameObject):
    def __init__(self, game_world, character, attack_data):
        t = character.transform
        self._facing = character.transform.facing
        position = (t.position[0] + (attack_data.position_offset[0] * self._facing), t.position[1] + attack_data.position_offset[1])
        super().__init__(game_world, position, t.scale)
        self._windup_time, self._hit_time, self._cooldown_time = attack_data.timings
        self._timings_hit = [False, False, False]
        self.data = attack_data
        self._life_time = 0.0
        self._character = character # player or enemy
        self._has_hit = False


    @property
    def character(self):
        return self._character

    def Awake(self):
        return super().Awake()
    
    def Start(self):
        #play sound effect here
        self.character.asset_pack.Play_attack_SFX(self.data.type)

        #play windup animation here (for windup time/duration)
        self.character.asset_pack.Play_attack_Animation(self.data.type, "doesn't matter rn")

        self._character.input_filter.append("attack")
        return super().Start()

    def Update(self, delta_time):
        self._life_time += delta_time
        self.Update_timings()
        return super().Update(delta_time)

    
    def Update_timings(self):
        if (self._life_time >= self._windup_time) & (not self._timings_hit[0]):
            self.Start_hit()
            self._timings_hit[0] = True
        elif (self._life_time >= (self._windup_time + self._hit_time)) & (not self._timings_hit[1]):
            self.Start_cooldown()
            self._timings_hit[1] = True
        elif (self._life_time >= (self._windup_time + self._hit_time + self._cooldown_time)) & (not self._timings_hit[2]):
            self.Stop_Attack()
            self._timings_hit[2] = True


    def Start_hit(self):
        #play hit animation
        #
        #adds colider and other components
        for component in self.data.Added_components(self._facing):
            self.Add_component(component)

    def Start_cooldown(self):
        #play cooldown animation

        #removes colider and other components
        for component in self.data.Removed_components():
            self.Remove_component(component)

    def Stop_Attack(self):
        self._character.input_filter.remove("attack")
        self.game_world.game_objects_to_remove.append(self)


    def OnCollision(self, other):
        # is a player or enemy that is not it's own
        if (not self._has_hit) & ((other.__class__.__name__ == "Player") | (other.__class__.__name__ == "Enemy")) & (other != self._character):
            self._has_hit = True
            if (not other.blocking) | self.data.ignores_block:
                other.Take_knockback(self.data.knockback, self._facing)
            return True
        return False