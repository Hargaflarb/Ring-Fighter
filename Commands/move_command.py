from Commands.Command import Command
import pygame

class MoveCommand(Command):
    def __init__(self, player, direction, speed):
        super().__init__()
        self._player = player
        self._direction = direction
        self._speed = speed

    def Execute(self, is_repeated, delta_time):
        if (not self._player.is_blocking_input) & (not self._player.is_blocking_movement):
            if self._direction != pygame.math.Vector2(0, 0):
                self._direction.normalize
            change = ((self._direction * self._speed))
            self._player.transform.translate(change*delta_time)
        
    
