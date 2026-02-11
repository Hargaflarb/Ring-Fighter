from GameObject import GameObject
import Components
import pygame
from abc import ABC


class Player(GameObject):
    def __init__(self, game_world, position):
        self.position = position
        self.game_world = game_world
        super().__init__(self.game_world, self.position)

        self.Add_component(Components.SpriteRenderer("temp playercharacter.png"))

 

