from Characters.Player import Player
from Characters.Enemy import Enemy
from Components import SpriteRenderer
import pygame

class Match_data():
    def __init__(self, game_world, map_type, player_type, enemy_type):
        self._game_world = game_world
        self.character_sprites = {} # not sure if this is needed
        self._player_type = player_type
        self._enemy_type = enemy_type
        self._map_type = map_type


    def Create_characters(self):
        characters = []

        characters.append(Player(self._game_world, pygame.math.Vector2(480, 360), 0.75, "right"))
        characters.append(Enemy(self._game_world, pygame.math.Vector2(800, 360), 0.75, "left", characters[0]))

        return characters


    def Get_map_spritesrenderes(self):
        sprite_renderers = []
        sprite_renderers.append(SpriteRenderer("temp playercharacter.png", "right"))
        sprite_renderers.append(SpriteRenderer("temp playercharacter.png", "left"))
        
        return sprite_renderers

