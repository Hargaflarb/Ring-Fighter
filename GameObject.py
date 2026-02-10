import pygame

class GameObject:
    def __init__(self,game_world):
        pygame.init()
        #self.sprite_image=pygame.image.load("assets\\image.png")
        self.sprite=pygame.sprite.Sprite()
        #self.sprite.rect=self.sprite_image.get_rect()
        self.game_world=game_world
    
    def Awake(self):
        pass

    def Start(self):
        pass
    def Update(self,delta_time):
        #self.game_world.Screen.blit(self.sprite_image,self.sprite.rect)
        pass