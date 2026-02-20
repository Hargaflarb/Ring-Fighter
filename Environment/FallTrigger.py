from GameObject import GameObject
from Characters.Player import Player
import pygame
from abc import ABC
from Components import Colider


class Fall_trigger(GameObject):
    def __init__(self, game_world):
        super().__init__(game_world, pygame.math.Vector2(640, 580), 1)
        self.Add_component(Colider((1000,50,1000,0), 3))
        self._triggered_characters = []


    def OnCollision(self, other):
        if ((other.__class__.__name__ == "Player") | (other.__class__.__name__ == "Enemy")) & (other not in self._triggered_characters):
            other.asset_pack.Play_Fall_SFX()
            other.asset_pack.Play_Fall_Animation()
            self._triggered_characters.append(other)
            