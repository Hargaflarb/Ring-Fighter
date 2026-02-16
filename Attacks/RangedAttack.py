from Attacks.Attack import Attack

class Ranged_attack(Attack):
    def __init__(self, game_world, character, attack_data):
        super().__init__(game_world, character, attack_data)
        self._character = character
        self._colided = False

    def Awake(self):
        pass
    
    def Start(self):
        return super().Start()

    def Update(self, delta_time):
        return super().Update(delta_time)

    def Start_hit(self):
        #play projektile animation
        super().Start_hit()


    def Start_cooldown(self):
        #play cooldown animation
        pass

    def Stop_Attack(self):
        # print(f"filters: {self.character.input_filter} !!!")
        self.character.input_filter.remove("attack")
        self.Is_done()

    def OnCollision(self, other):
        if super().OnCollision(other) | (other.Get_component("Colider").colider_type == 1):
            self._colided = True
            self.Is_done()
            self.Remove_all_components()


    def Is_done(self):
        if (self._colided) & (not ("attack" in self.character.input_filter)):
            self.game_world.game_objects_to_remove.append(self)
