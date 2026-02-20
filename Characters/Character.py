from GameObject import GameObject
from Components import SpriteRenderer
from Components import Animator
from CharacterAssetsPack import Character_assets_pack
from random import Random
from abc import ABC
import pygame

class Character(GameObject):
    def __init__(self, game_world, position, scale, direction, character_name, difficulty):
        super().__init__(game_world, position, scale)
        self._random = Random()
        self._crouching = False
        self._blocking = False
        self._moving = False #not 100% accurate
        self._character_name = character_name
        self._direction = direction
        self.input_filter = []
        
        sr = self.Add_component(SpriteRenderer("Malthe\MaltheIdle\malthe idle 4.png"))
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(), sr.sprite_image.get_height())
        self.Add_component(Animator(sr))

        
        sr.Flip(sr.sprite_image, self._direction)

        animator = self.Get_component("Animator")
        self._asset_pack = Character_assets_pack(animator, self._character_name)
        self._asset_pack.Add_Animations()
        self._asset_pack.Set_Idle_To_Default()
        self._asset_pack.Play_Idle_Animation()

        self._time_since_action = 0 # used for taunt
        self._taunt_wait_time = 10
        self.Reroll_taunt_time()

        damage_mod = 1

        if difficulty == "Easy":
            damage_mod = 1
        elif difficulty == "Normal":
            damage_mod = 2
        elif difficulty == "Boss":
            damage_mod = 3
        else:
            damage_mod = 1

        
        self.attack_types = {}
        self.attack_types["standard_attack"] = Attack_Data(Attack_type.StandardAttack, (0.1,0.2,0.1), (50,30), (-100,-180), (damage_mod*100,0), False)
        self.attack_types["low_attack"] = Attack_Data(Attack_type.LowAttack, (0.5,0.2,0.3), (50,40), (-80,0), (damage_mod*350,0), True)
        self.attack_types["down_attack"] = Attack_Data(Attack_type.DownSmash, (0.2,0.1,0.8), (40,110), (-65,-60), (damage_mod*350,0), False)
        self.attack_types["up_attack"] = Attack_Data(Attack_type.UpSmash, (0.3,0.2,0.3), (40,70), (-80,-65), (200,100), False)
        self.attack_types["ranged_attack"] = Attack_Data(Attack_type.Ranged, (0.7,0.0,0.8), (50,50), (-80,-180), (damage_mod*100,0), False)


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
    def moving(self):
        return self._moving

    @moving.setter
    def moving(self, value):
        self._moving = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    
    @property
    def asset_pack(self):
        return self._asset_pack
    
    def Update(self, delta_time):
        self._time_since_action += delta_time
        if self._time_since_action >= self._taunt_wait_time:
            self._asset_pack.Play_Taunt_SFX()
            self._time_since_action = 0
            self.Reroll_taunt_time()

        if (self._asset_pack.current_animation_ID == "W") & (not self._moving): # horrible solution but it works
            self._asset_pack.Play_Default_Animation()
            print("not move")
        
        self._moving = False

        super().Update(delta_time)

    def Action_notification(self):
        self._time_since_action = 0


    def Crouch_toggle(self):
        old_rect = self.Get_component("Colider").rect
        if self._crouching: #stops crouching
            self.Get_component("Colider").rect = (old_rect[0], old_rect[1]*2, old_rect[2], old_rect[3])
            self.input_filter.remove("crouch")
            self._asset_pack.Set_Idle_To_Default()
        else: #starts crouching
            self.Get_component("Colider").rect = (old_rect[0], old_rect[1]/2, old_rect[2], old_rect[3])
            self.input_filter.append("crouch")
            self._asset_pack.Set_Crouch_To_Default()
        self._crouching = not self._crouching
 

    def Block_toggle(self):
        if self._blocking: #stops blocking
            self.input_filter.remove("block")
            self._asset_pack.Play_Default_Animation()
        else: #starts blocking
            self.input_filter.append("block")
            self._asset_pack.Play_Block_Animation()
        self._blocking = not self._blocking

    def Take_knockback(self, knockback, facing):
        # resets taunt-timer
        self._time_since_action = 0

        # play hit sound
        self._asset_pack.Play_Hit_SFX()

        # play hit animation
        self._asset_pack.Play_Hit_Animation()

        self.Get_component("Momentum").Give_Momentum(knockback, facing)

    
    def Reroll_taunt_time(self):
        self._taunt_wait_time = self._random.randint(5, 10)