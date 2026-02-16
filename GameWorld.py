import pygame
from GameObject import GameObject
from Components import Momentum
from Components import Gravity
from Components import Colider
from Components import SpriteRenderer
from Components import Animator
from Characters.Player import Player
from Characters.Enemy import Enemy
from Environment.Void import Void
from SoundManager import SoundManager
from Event import Event
from Menu import Start_menu
from Menu import Button

class Game_World:
    def __init__(self)->None:
        pygame.init()
        self.screen=pygame.display.set_mode((1280,720))
        self.running=True
        self.clock=pygame.time.Clock()
        self.showing_menu=True
        self._events = {}

        self.active_game_objects=[]
        self.game_objects_to_add=[]
        self.game_objects_to_remove=[]

        self.menu= Start_menu(self.screen)
        

        player = Player(self, pygame.math.Vector2(640, 360), 0.5)
        self.game_objects_to_add.append(player)
        enemy = Enemy(self, pygame.math.Vector2(800, 360), 0.5)
        self.game_objects_to_add.append(enemy)

        floor = GameObject(self, pygame.math.Vector2(640, 720), 0.5)
        floor.Add_component(Colider((500, 300, 500, 0), 1))
        self.game_objects_to_add.append(floor)

        self.game_objects_to_add.append(Void(self))


        sm=SoundManager()
        sm.Add_sfx("Ding","ding-36029.mp3",0.5)
        #sm.Play_sfx("Ding")
        sm.Add_music("spk","The Oh Hellos - Soldier, Poet, King (Official Lyric Video).mp3",0.5)
        sm.Play_music("spk")
        sm2=SoundManager()
        #sm2.Stop_music()


    @property
    def Screen(self):
            return self.screen
            
    def Awake(self):
        for gameobject in self.active_game_objects:
            gameobject.Awake()
    def Start(self):
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
            #basic state, can be removed later
            if self.showing_menu:
                #also add menu background here
                returned_string=self.menu.draw_menu()
                if returned_string=="start":
                    self.showing_menu=False
                elif returned_string=="quit":
                    self.running=False
            else:
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

    def Make_event(self, name):
        new_event = Event()
        self._events[name] = new_event
        return new_event
    
    def Get_event(self, name):
        if name in self._events.keys():
            return self._events[name]
        
    def Delete_event(self, name):
        if name in self._events.keys():
            del self._events[name]
        



gw=Game_World()
gw.Awake()
gw.Start()
gw.Update()