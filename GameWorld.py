import pygame
from GameObject import GameObject

class Game_World:
    def __init__(self)->None:
        pygame.init()
        self.screen=pygame.display.set_mode((1280,720))
        self.running=True
        self.clock=pygame.time.Clock()

        self.active_game_objects=[]
        self.active_game_objects.append(GameObject(self))


    @property
    def Screen(self):
            return self.screen
            
    def Awake(self):
        pass
    def Start(self):
        pass
    def Update(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
            
            delta_time=self.clock.tick(60)/1000.0

            #background colour
            self.screen.fill("green")

            #add things to draw
            #self.screen.blit(self.sprite_image,self.sprite.rect)
            for gameobject in self.active_game_objects:
                gameobject.Update(delta_time)
            
            #draws to screen
            pygame.display.flip()

            self.clock.tick(60)
        
        pygame.quit()

gw=Game_World()
gw.Awake()
gw.Start()
gw.Update()