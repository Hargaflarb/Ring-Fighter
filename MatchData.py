from Characters.Player import Player
from Characters.Enemy import Enemy
from Components import SpriteRenderer
import pygame

class Match_data():
    def __init__(self, game_world, map_type, player_type, enemy_type, difficulty):
        self._game_world = game_world
        self.character_sprites = {} # not sure if this is needed
        self._player_type = player_type # their name. can be changed or expanded
        self._enemy_type = enemy_type # their name. can be changed or expanded
        self._map_type = map_type
        self._difficulty = difficulty


    def Create_characters(self):
        characters = []

        characters.append(Player(self._game_world, pygame.math.Vector2(480, 360), 0.75, 1, self._player_type, self._difficulty))
        characters.append(Enemy(self._game_world, pygame.math.Vector2(800, 360), 0.75, -1, characters[0], self._enemy_type, self._difficulty))

        return characters


    def Get_map_spritesrenderes(self):
        sprite_renderers = []
        sprite_renderers.append(SpriteRenderer("Maps\\mapice.png"))
        sprite_renderers.append(SpriteRenderer("temp playercharacter.png"))
        
        return sprite_renderers

