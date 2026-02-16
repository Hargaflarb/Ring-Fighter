from Commands.Command import Command
from Attacks.AttackData import Attack_Data
from Attacks.Attack import Attack
import pygame

class Attack_command(Command):
    def __init__(self, player, direction, attack_data, crouched_attack):
        super().__init__()
        self._player = player
        self._direction = direction
        self._crouched_attack = crouched_attack
        self._attack_data = attack_data


    def Execute(self, is_repeated, delta_time):
        if (not is_repeated) & (not self._player.is_blocking_input) & (self._player.crouching == self._crouched_attack):
            the_attack = Attack(self._player.game_world, self._player, self._attack_data)
            self._player.game_world.game_objects_to_add.append(the_attack)

