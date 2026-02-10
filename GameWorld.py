import pygame
from GameObject import GameObject
from Components import Momentum
from Components import Gravity

class Game_World:
    def __init__(self)->None:
        pygame.init()
        self.screen=pygame.display.set_mode((1280,720))
        self.running=True
        self.clock=pygame.time.Clock()

        self.active_game_objects=[]
        self.game_objects_to_add=[]
        self.game_objects_to_remove=[]
        #self.active_game_objects.append(GameObject(self))


    @property
    def Screen(self):
            return self.screen
            
    def Awake(self):
        pass
    def Start(self):
        gm = GameObject(self, (10,10))
        gm.Add_component(Momentum())
        gm.Add_component(Gravity())
        self.game_objects_to_add.append(gm)

    def Update(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
            
            #add & remove gameobjects during runtime
            for gameobject in self.game_objects_to_add:
                if gameobject not in self.active_game_objects:
                    self.active_game_objects.append(gameobject)
            self.game_objects_to_add.clear()
            for gameobject in self.game_objects_to_remove:
                if gameobject in self.active_game_objects:
                    self.active_game_objects.remove(gameobject)
            self.game_objects_to_remove.clear()
            
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

    def Colision(self):
        for obj1 in self.active_game_objects:
            for obj2 in self.active_game_objects:
                if obj1 != obj2: # aren't the same
                    col1 = obj1.Get_component("Colider")
                    col2 = obj2.Get_component("Colider")
                    if col1 != None & col2 != None: # both has coliders
                        col1.Check_collision(col2)




gw=Game_World()
gw.Awake()
gw.Start()
gw.Update()