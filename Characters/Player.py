from Characters import Character
import Components
import pygame
from Commands import MoveCommand


class Player(Character):
    def __init__(self):
        super.__init__()
        self._speed = 50
        self.position = pygame.math.Vector2(0,0)
        

        self._inputhandler = Components.Input_Handler(self)
    

    def Start(self):
        self._inputhandler.Add_Command(pygame.K_d, MoveCommand(self, pygame.math.Vector2(0,1)))

 

    