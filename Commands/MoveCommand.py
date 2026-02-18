from Commands.Command import Command
import pygame

class MoveCommand(Command):
    def __init__(self, player, direction, speed):
        super().__init__()
        self._player = player
        self._direction = direction
        self._speed = speed

    @property
    def blocking_filters(self):
        return ["block", "crouch", "attack"]

    def Execute(self, is_repeated, delta_time):
        if self.Pass_filter(self._player.input_filter):
            if self._direction != pygame.math.Vector2(0, 0):
                self._direction.normalize
            change = ((self._direction * self._speed))
            self._player.transform.translate(change*delta_time)

            # tells character that an action has been made
            self._player.Action_notification()
    
