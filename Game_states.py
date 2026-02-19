from enum import Enum

class Game_States(Enum):
    Null=1
    Gameplay=2
    Main_menu=3
    End_screen_win=4
    End_screen_lose=5
    Character_select=6