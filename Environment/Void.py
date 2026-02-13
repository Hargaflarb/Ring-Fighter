from GameObject import GameObject
import Components
import pygame
from abc import ABC
from Components import Colider


class Void(GameObject):
    def __init__(self, game_world):
        super().__init__(game_world, pygame.math.Vector2(640, 720), 1)
        self.Add_component(Colider((1000,50,1000,0), 3))


    def OnCollision(self, other):
        if other.__class__.__name__ == "Player":
            print("Player died.")
            self.game_world.game_objects_to_remove.append(other)
            # call methodes here?





 

