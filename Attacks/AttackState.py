from enum import Enum


class Attack_state(Enum):
    Inactive = 0
    WindUp = 1
    Hitting = 2
    Cooldown = 3

