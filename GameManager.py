from GameObject import GameObject
from Characters.Player import Player
from Characters.Enemy import Enemy
from Environment.Void import Void
from Environment.FallTrigger import Fall_trigger
from Components import Colider
from Components import SpriteRenderer
from MatchData import Match_data
from random import Random
from Game_states import Game_States
from SoundManager import SoundManager
import pygame


class Game_manager():
    def __init__(self, game_world):
        self._game_world = game_world
        self._characters = []
        self._rounds_won = [0,0]
        self._score=0
        player=None
        self._current_match = -1

        self._match_datas = []
    
    @property
    def Score(self):
        return self._score
    
    @Score.setter
    def Score(self,value):
        self._score=value

    def End_round(self, winner): #1 = player, 2 = enemy
        if winner == 1: # player
            self._rounds_won[0] += 1
            self._score+=50
            print("player won the round")
        elif winner == 2: # enemy
            self._rounds_won[1] += 1
            self._score-=20
            print("player lost the round")
        self.Despawn_Characters()
        self.Next_round()

    def Next_round(self):
        if self._rounds_won[0] >= 2:
            print("player won the match")
            self._score+=200
            self.Next_match()
        elif self._rounds_won[1] >= 2:
            print("player lost the match")
            sm=SoundManager.instance
            sm.Play_music("lose")
            self._game_world.game_state=Game_States.End_screen_lose
        else:
            self.Spawn_Characters()
            # load new round

    def Next_match(self):
        self._rounds_won = [0,0]
        self._current_match += 1
        if self._current_match >= 2:
            print("player won the game")
            sm=SoundManager.instance
            sm.Play_music("win")
            self._game_world.game_state=Game_States.End_screen_win
        else:
            self.Set_up_arena()
            self.Next_round()


    def Start_game(self,character):
        print("new game started")
        self._game_world.Restart_game()
        self._current_match = -1
        self._score=0
        self._match_datas.clear()
        self._match_datas.append(Match_data(self._game_world, "some type", character,"Echo"))
        self._match_datas.append(Match_data(self._game_world, "some type", character,"Emma"))
        self._match_datas.append(Match_data(self._game_world, "some type", character,"Malthe"))
        sm=SoundManager.instance
        sm.Play_music("fighting")
        self._game_world.game_state=Game_States.Gameplay
        self.Next_match()

    def Set_up_arena(self):
        sprite_renderers = self._match_datas[self._current_match].Get_map_spritesrenderes()
        
        background = GameObject(self._game_world, pygame.math.Vector2(640, 720), 1)
        background.Add_component(sprite_renderers[1])
        self._game_world.game_objects_to_add.append(background)

        floor = GameObject(self._game_world, pygame.math.Vector2(625, 720), 1)
        floor.Add_component(Colider((410, 200, 440, 0), 1))
        floor.Add_component(sprite_renderers[0])
        self._game_world.game_objects_to_add.append(floor)

        wall = GameObject(self._game_world, pygame.math.Vector2(0, 720), 1)
        wall.Add_component(Colider((10, 720, 10, 0), 1))
        self._game_world.game_objects_to_add.append(wall)

        wall = GameObject(self._game_world, pygame.math.Vector2(1280, 720), 1)
        wall.Add_component(Colider((10, 720, 10, 0), 1))
        self._game_world.game_objects_to_add.append(wall)

        self._game_world.game_objects_to_add.append(Void(self._game_world))
        self._game_world.game_objects_to_add.append(Fall_trigger(self._game_world))

    def Spawn_Characters(self):
        characters = self._match_datas[self._current_match].Create_characters()
        self._game_world.game_objects_to_add.append(characters[0])
        self._game_world.game_objects_to_add.append(characters[1])
        self._characters.append(characters[0])
        self._characters.append(characters[1])
    
    def Despawn_Characters(self):
        for character in self._characters:
            self._game_world.game_objects_to_remove.append(character)


    def Get_rounds_won_string(self):
        return f"{self._rounds_won[0]} - {self._rounds_won[1]}"