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

    @property
    def blocking_filters(self):
        return ["block", "attack"]

    def Execute(self, is_repeated, delta_time):
        if (not is_repeated) & (self.Pass_filter(self._player.input_filter)) & (self._player.crouching == self._crouched_attack):
            the_attack = self._attack_data.Make_attack_object(self._player.game_world, self._player)
            self._player.game_world.game_objects_to_add.append(the_attack)

            # tells character that an action has been made
            self._player.Action_notification()


