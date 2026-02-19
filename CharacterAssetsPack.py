from SoundManager import SoundManager
from random import Random
from Attacks.AttackType import Attack_type

class Character_assets_pack():
    def __init__(self, animator, character_name):
        self._character_name = character_name
        self._animator = animator
        self.current_animation_ID = None
        self.default_animation_ID = None

        self._random = Random()
        self._sm = SoundManager.instance

    def Play_attack_SFX(self, attack_type):
        if attack_type == Attack_type.DownSmash:
            self.Play_DownSmash_SFX()
        elif attack_type == Attack_type.LowAttack:
            self.Play_LowAttack_SFX()
        elif attack_type == Attack_type.UpSmash:
            self.Play_UpSmash_SFX()
        elif attack_type == Attack_type.StandardAttack:
            self.Play_StandardAttack_SFX()
        elif attack_type == Attack_type.Ranged:
            self.Play_Ranged_SFX()

    def Play_attack_Animation(self, attack_type, attack_state):
        if attack_type == Attack_type.DownSmash:
            self.Play_DownSmash_Animation(attack_state)
        elif attack_type == Attack_type.LowAttack:
            self.Play_LowAttack_Animation(attack_state)
        elif attack_type == Attack_type.UpSmash:
            self.Play_UpSmash_Animation(attack_state)
        elif attack_type == Attack_type.StandardAttack:
            self.Play_StandardAttack_Animation(attack_state)
        elif attack_type == Attack_type.Ranged:
            self.Play_Ranged_Animation(attack_state)


    def Play_DownSmash_SFX(self):
        self._sm.Play_sfx(f"{self._character_name}DS")

    def Play_LowAttack_SFX(self):
        self._sm.Play_sfx(f"{self._character_name}LA")

    def Play_UpSmash_SFX(self):
        self._sm.Play_sfx(f"{self._character_name}US")

    def Play_StandardAttack_SFX(self):
        self._sm.Play_sfx(f"{self._character_name}SA")

    def Play_Ranged_SFX(self):
        self._sm.Play_sfx(f"{self._character_name}R")

    def Play_Fall_SFX(self):
        self._sm.Play_sfx(f"{self._character_name}F")

    def Play_Hit_SFX(self):
        num = self._random.randint(1,2)
        self._sm.Play_sfx(f"{self._character_name}H{num}")

    def Play_Taunt_SFX(self):
        num = self._random.randint(1,2)
        self._sm.Play_sfx(f"{self._character_name}T{num}")


    def Play_DownSmash_Animation(self, attack_state):
        self._animator.Play_animation(f"{self._character_name}DS", False)
        self.current_animation_ID = "DS"

    def Play_LowAttack_Animation(self, attack_state):
        self._animator.Play_animation(f"{self._character_name}LA", False)
        self.current_animation_ID = "LA"

    def Play_UpSmash_Animation(self, attack_state):
        self._animator.Play_animation(f"{self._character_name}US", False)
        self.current_animation_ID = "US"

    def Play_StandardAttack_Animation(self, attack_state):
        self._animator.Play_animation(f"{self._character_name}SA", False)
        self.current_animation_ID = "SA"

    def Play_Ranged_Animation(self, attack_state):
        self._animator.Play_animation(f"{self._character_name}R", False)
        self.current_animation_ID = "R"

    def Play_Fall_Animation(self):
        self._animator.Play_animation(f"{self._character_name}F", True)
        self.current_animation_ID = "F"

    def Play_Hit_Animation(self):
        self._animator.Play_animation(f"{self._character_name}H", False)
        self.current_animation_ID = "H"

    def Play_Idle_Animation(self): #outdated
        self._animator.Play_animation(f"{self._character_name}I", True)

    def Play_Crouch_Animation(self): #outdated
        self._animator.Play_animation(f"{self._character_name}C", True)

    def Play_Walk_Animation(self):
        self._animator.Play_animation(f"{self._character_name}W", True)
        self.current_animation_ID = "W"

    def Play_Block_Animation(self):
        self._animator.Play_animation(f"{self._character_name}B", True)
        self.current_animation_ID = "B"


    def Set_Idle_To_Default(self):
        self._animator.Set_default_animation(f"{self._character_name}I")
        self.default_animation_ID = "I"
        self._animator.Stop_animation()

    def Set_Crouch_To_Default(self):
        self._animator.Set_default_animation(f"{self._character_name}C")
        self.default_animation_ID = "C"
        self._animator.Stop_animation()

    def Play_Default_Animation(self):
        self._animator.Stop_animation()
        self.current_animation_ID = self.default_animation_ID


    def Add_Animations(self):
        name = self._character_name

        # standard attack
        SA = []
        for i in range(1,4+1):
            SA.append(f"{name}\\{name}Attack\\{name} hit{i}.png")
        self._animator.Add_animation(f"{name}SA",SA)

        # low attack
        LA = []
        for i in range(1,10+1):
            LA.append(f"{name}\\{name}Crouchattack\\{name} crouch attack {i}.png")
        self._animator.Add_animation(f"{name}LA",LA)

        # down smash
        DS = []
        for i in range(1,8+1):
            DS.append(f"{name}\\{name}Downsmash\\{name} down smash {i}.png")
        self._animator.Add_animation(f"{name}DS",DS)

        # up smash
        # US = []
        # for i in range(1,8+1):
        #     US.append(f"{name}\\{name}Upsmash\\{name} up smash {i}.png")
        # self._animator.Add_animation(f"{name}US",US)

        # ranged
        R = []
        for i in range(1,13+1):
            R.append(f"{name}\\{name}Ranged\\{name} ranged {i}.png")
        self._animator.Add_animation(f"{name}R",R)


        # block
        self._animator.Add_animation(f"{name}B",[f"{name}\\{name}Block\\{name} block.png"])

        # crouch
        self._animator.Add_animation(f"{name}C",[f"{name}\\{name}Crouch\\{name} crouch.png"])

        # fall
        self._animator.Add_animation(f"{name}F",[f"{name}\\{name}Fall\\{name} fall.png"])

        # hit
        self._animator.Add_animation(f"{name}H",[f"{name}\\{name}Hit\\{name} hit.png"])

        # idle (not standardized - Echo has 6)
        I = []
        for i in range(1,4+1):
            I.append(f"{name}\\{name}Idle\\{name} idle {i}.png")
        if name == "Echo":
            I.append(f"{name}\\{name}Idle\\{name} idle {5}.png")
            I.append(f"{name}\\{name}Idle\\{name} idle {6}.png")
        self._animator.Add_animation(f"{name}I",I)

        # walk (not standardized - Malthe has 5)
        W = []
        for i in range(1,5+1):
            W.append(f"{name}\\{name}Walk\\{name} walk {i}.png")
        if (name == "Echo") | (name == "Emma"):
            I.append(f"{name}\\{name}Walk\\{name} walk {6}.png")
        self._animator.Add_animation(f"{name}W",W)
