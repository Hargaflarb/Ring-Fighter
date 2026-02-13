import pygame
from GameObject import GameObject
from Components import Momentum
from Components import Gravity
from Components import Colider
from Components import SpriteRenderer
from Components import Animator
from Characters.player import Player
from SoundManager import SoundManager

class Game_World:
    def __init__(self)->None:
        pygame.init()
        self.screen=pygame.display.set_mode((1280,720))
        self.running=True
        self.clock=pygame.time.Clock()

        self.active_game_objects=[]
        self.game_objects_to_add=[]
        self.game_objects_to_remove=[]
        # player=GameObject(self,(1000,20))
        # self.game_objects_to_add.append(player)
        # #this could certainly be better
        # sr=player.Add_component(SpriteRenderer("temp playercharacter.png"))
        # an=player.Add_component(Animator(sr))
        # #could there be a way to add a folder without adding every frame? seems like that would be useful
        # an.Add_animation("TestWalk","temp playercharacter anim\\playerWalkShotgun0000.png",
        # "temp playercharacter anim\\playerWalkShotgun0001.png","temp playercharacter anim\\playerWalkShotgun0002.png",
        # "temp playercharacter anim\\playerWalkShotgun0003.png","temp playercharacter anim\\playerWalkShotgun0004.png",
        # "temp playercharacter anim\\playerWalkShotgun0005.png","temp playercharacter anim\\playerWalkShotgun0006.png",
        # "temp playercharacter anim\\playerWalkShotgun0007.png","temp playercharacter anim\\playerWalkShotgun0008.png",
        # "temp playercharacter anim\\playerWalkShotgun0009.png","temp playercharacter anim\\playerWalkShotgun0010.png")

        # an.Play_animation("TestWalk")
        # #this is just for testing purposes, feel free to remove

        player = Player(self, pygame.math.Vector2(100, 100))
        self.game_objects_to_add.append(player)


        sm=SoundManager()
        sm.Add_sfx("Ding","ding-36029.mp3",0.5)
        #sm.Play_sfx("Ding")
        sm.Add_music("spk","The Oh Hellos - Soldier, Poet, King (Official Lyric Video).mp3",0.5)
        sm.Play_music("spk")
        sm2=SoundManager()
        sm2.Stop_music()


    @property
    def Screen(self):
            return self.screen
            
    def Awake(self):
        for gameobject in self.active_game_objects:
            gameobject.Awake()
    def Start(self):
        # for tests
        #gm = GameObject(self, (1.99,4))
        #gm.Add_component(Momentum())
        #gm.Add_component(Gravity())
        #gm.Add_component(Colider((-1,-1,1,1)))
        #self.game_objects_to_add.append(gm)

        #gm2 = GameObject(self, (0,0))
        #gm2.Add_component(Colider((-1,-1,1,1)))
        #self.game_objects_to_add.append(gm2)


        for gameobject in self.active_game_objects:
            gameobject.Start()
    def Update(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
            
            #add & remove gameobjects during runtime
            for gameobject in self.game_objects_to_add:
                if gameobject not in self.active_game_objects:
                    gameobject.Awake()
                    gameobject.Start()
                    self.active_game_objects.append(gameobject)
                    gameobject.Awake()
                    gameobject.Start()
            self.game_objects_to_add.clear()
            for gameobject in self.game_objects_to_remove:
                if gameobject in self.active_game_objects:
                    self.active_game_objects.remove(gameobject)
            self.game_objects_to_remove.clear()
            
            self.Collision()

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

    def Collision(self):
        for i, obj1 in enumerate(self.active_game_objects):
            for j in range(i + 1, len(self.active_game_objects)):
                    col1 = obj1.Get_component("Colider")
                    col2 = self.active_game_objects[j].Get_component("Colider")
                    if (col1 != None) & (col2 != None): # both has coliders
                        if (col1.Check_collision(col2)): # does colide
                            col1.On_collision(col2)
                            col2.On_collision(col1)




gw=Game_World()
gw.Awake()
gw.Start()
gw.Update()