from GameObject import GameObject

class Attack(GameObject):
    def __init__(self, game_world, character, attack_data):
        t = character.transform
        position = (t.position[0] + (attack_data.position_offset[0] * t.facing), t.position[1] + attack_data.position_offset[1])
        super().__init__(game_world, position, t.scale)
        self._windup_time, self._hit_time, self._cooldown_time = attack_data.timings
        self._timings_hit = [False, False]
        self.data = attack_data
        self._life_time = 0.0



    def Awake(self):
        return super().Awake()
    
    def Start(self):
        #play sound effect here
        #play windup animation here (for windup time/duration)
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
            pass
        elif self._life_time >= (self._windup_time + self._hit_time + self._cooldown_time):
            self.game_world.game_objects_to_remove.append(self) # don't do this for ranged


    def Start_hit(self):
        #play hit animation

        #adds colider and other components
        for component in self.data.Added_components(1): #member to fix the facing here
            self.Add_component(component)

    def Start_cooldown(self):
        #play cooldown animation

        #removes colider and other components
        for component in self.data.Removed_components():
            self.Add_component(component)




