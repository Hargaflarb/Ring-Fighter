from SoundManager import SoundManager
from random import Random
from Attacks.AttackType import Attack_type

class Character_sound_pack():
    def __init__(self, character_name):
        self._character_name = character_name
        self._random = Random()
        self._sm = SoundManager.instance

    def Play_attack_SFX(self, attack_type):
        if attack_type == Attack_type.DownSmash:
            self.Play_DownSmash()
        elif attack_type == Attack_type.LowAttack:
            self.Play_LowAttack()
        elif attack_type == Attack_type.UpSmash:
            self.Play_UpSmash()
        elif attack_type == Attack_type.StandardAttack:
            self.Play_StandardAttack()
        elif attack_type == Attack_type.Ranged:
            self.Play_Ranged()


    def Play_DownSmash(self):
        self._sm.Play_sfx(f"{self._character_name}DS")

    def Play_LowAttack(self):
        self._sm.Play_sfx(f"{self._character_name}LA")

    def Play_UpSmash(self):
        self._sm.Play_sfx(f"{self._character_name}US")

    def Play_StandardAttack(self):
        self._sm.Play_sfx(f"{self._character_name}SA")

    def Play_Ranged(self):
        self._sm.Play_sfx(f"{self._character_name}R")

    def Play_Fall(self):
        self._sm.Play_sfx(f"{self._character_name}F")

    def Play_Hit(self):
        self._sm.Play_sfx(f"{self._character_name}H")

    def Play_Taunt(self):
        num = self._random.randint(1,2)
        self._sm.Play_sfx(f"{self._character_name}T{num}")



