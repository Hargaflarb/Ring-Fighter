from Commands.Command import Command
from Attacks.AttackData import Attack_Data
# from Characters.Player import Player
from Attacks.Attack import Attack
import pygame

class Attack_command(Command):
    def __init__(self, player, direction):
        super().__init__()
        self._player = player
        self._direction = direction
        self._attack_data = Attack_Data("attack name", (0.5,0.2,0.5), (20,5), (20,40))

    def Execute(self, delta_time):
        the_attack = Attack(self._player.game_world, self._player, self._attack_data)
        self._player.game_world.game_objects_to_add.append(the_attack)

