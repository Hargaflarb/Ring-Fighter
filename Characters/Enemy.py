from GameObject import GameObject
from Characters.Character import Character
import Components
from Components import Momentum
from Components import Gravity
from Components import Colider
from AI.FSM import FSM
from AI.Null_State import Null_State
from AI.Idle_State import Idle_State
from AI.Attack_State import Attack_State
from AI.AI_Conditions import AI_Conditions
import pygame


class Enemy(Character):
    def __init__(self, game_world, position, scale, direction, opponent, character_name):
        super().__init__(game_world, position, scale, direction, character_name)

        self._speed = 250
        self._opponent = opponent
        sr = self.Add_component(Components.SpriteRenderer("Malthe\MaltheIdle\malthe idle 4.png"))
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(), sr.sprite_image.get_height())

        input_handler = self.Add_component(Components.Input_Handler(self))

        self.Add_component(Momentum())
        self.Add_component(Gravity())
        self.Add_component(Colider((self._sprite_size[0]/3,self._sprite_size[1],self._sprite_size[0]/3,0), 2))

        self.fsm = self.Add_component(FSM(Null_State(self, self._opponent), self))

        self.fsm.Add_Transition(type(Null_State(self, self._opponent)), AI_Conditions.Idle, Idle_State(self, self._opponent))
        self.fsm.Add_Transition(type(Idle_State(self, self._opponent)), AI_Conditions.Attack, Attack_State(self, self._opponent))
        self.fsm.Add_Transition(type(Attack_State(self, self._opponent)), AI_Conditions.Idle, Idle_State(self, self._opponent))