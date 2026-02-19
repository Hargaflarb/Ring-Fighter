from Commands.Command import Command
from Attacks.AttackData import Attack_Data
from Attacks.Attack import Attack
import pygame

class Crouch_command(Command):
    def __init__(self, player):
        super().__init__()
        self._player = player

    @property
    def blocking_filters(self):
        return ["block", "attack"]

    def Execute(self, is_repeated, delta_time):
        if (not is_repeated) & self.Pass_filter(self._player.input_filter):
            self._player.Crouch_toggle()
            
            # tells character that an action has been made
            self._player.Action_notification()


