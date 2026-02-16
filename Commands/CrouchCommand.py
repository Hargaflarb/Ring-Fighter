from Commands.Command import Command
from Attacks.AttackData import Attack_Data
from Attacks.Attack import Attack
import pygame

class Crouch_command(Command):
    def __init__(self, player):
        super().__init__()
        self._player = player

    def Execute(self, is_repeated, delta_time):
        if (not is_repeated) & (not self._player.is_blocking_input):
            self._player.Crouch_toggle()

