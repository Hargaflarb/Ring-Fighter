from GameObject import GameObject
from Characters.Character import Character
import Components
import pygame
from AI.FSM import FSM
from AI.Idle_State import Idle_State
from AI.Attack_State import Attack_State
from AI.Null_State import Null_State
from AI.AI_Conditions import AI_Conditions
from Components import Momentum
from Components import Gravity
from Components import Colider
import pygame


class Enemy(Character):
    def __init__(self, game_world, position, scale):
        super().__init__(game_world, position, scale)

        self._opponent = opponent
        self.speed = 50
        sr = self.Add_component(Components.SpriteRenderer("temp playercharacter.png"))
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(), sr.sprite_image.get_height())
        self.fsm = self.Add_component(FSM(Idle_State(self, self._opponent), self))

        self.Add_component(Components.Momentum())
        self.Add_component(Components.Gravity())
        self.Add_component(Components.Colider((self._sprite_size[0]/2,self._sprite_size[1],self._sprite_size[0]/2,0), 2))

        if difficulty == "Easy":
            print("Easy")
        elif difficulty == "Normal":
            print("Normal")
        elif difficulty == "Boss":
            print("Boss")

        self.fsm.Add_Transition(type(Null_State(self)), AI_Conditions.Idle, Idle_State(self, self._opponent))
        self.fsm.Add_Transition(type(Idle_State(self, self._opponent)), AI_Conditions.Attack, Attack_State(self, self._opponent))
        self.fsm.Add_Transition(type(Attack_State(self, self._opponent)), AI_Conditions.Idle, Idle_State(self, self._opponent))
        
    def Move(self, direction, delta_time):
        if direction != pygame.math.Vector2(0, 0):
           direction.normalize
        change = ((direction * self.speed))
        self.transform.translate(change*delta_time)

        self.Add_component(Momentum())
        self.Add_component(Gravity())
        self.Add_component(Colider((self._sprite_size[0]/3,self._sprite_size[1],self._sprite_size[0]/3,0), 2))

