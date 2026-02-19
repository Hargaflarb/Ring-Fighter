import pygame
from SoundManager import SoundManager
from GameManager import Game_manager

class Start_menu():
    #singleton code; creates a new instance if none exist, otherwise returns the instance
    def __new__(cls,screen):
        if not hasattr(cls,'instance'):
            cls.instance=super().__new__(cls)
        return cls.instance
    
    def __init__(self,screen):
        self.screen=screen
        self.font=pygame.font.SysFont("arialblack",60)
        self.text_colour=(0,0,0)
        self.showing_options=False
        self.music_volume_number=10
        self.sfx_volume_number=10
        self.create_menu()
        self.create_options()
        self.sm=SoundManager()

    def create_menu(self):
        start_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\startbtn.png")
        self.start_button=Button(self.screen.width/2,150,start_btn_image,None,1)
        options_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\optionsbtn.png")
        self.options_button=Button(self.screen.width/2,300,options_btn_image,None,1)
        quit_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\quitbtn.png")
        self.quit_button=Button(self.screen.width/2,450,quit_btn_image,None,1)

    def create_options(self):
        back_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\backbtn.png")
        self.back_button=Button(200,self.screen.height-150,back_btn_image,None,1)
        plus_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\plusbtn.png")
        self.plus_music_button=Button(self.screen.width/2-200,120,plus_btn_image,None,1)
        minus_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\minusbtn.png")
        self.minus_music_button=Button(self.screen.width/2+200,120,minus_btn_image,None,1)

        self.plus_sfx_button=Button(self.screen.width/2-200,350,plus_btn_image,None,1)
        self.minus_sfx_button=Button(self.screen.width/2+200,350,minus_btn_image,None,1)
        
    def draw_text(self,text,x,y):
        img=self.font.render(text,True,self.text_colour)
        self.screen.blit(img,(x,y))

    def draw_menu(self):
        if self.showing_options==False:
            if self.start_button.draw(self.screen):
                return "start"
            if self.options_button.draw(self.screen):
                self.showing_options=True
            if self.quit_button.draw(self.screen):
                return "quit"
        else:
            self.draw_text("Music volume",self.screen.width/2-300,0)
            if self.plus_music_button.draw(self.screen):
                if(self.music_volume_number<10):
                    self.music_volume_number+=1
                    new_volume=float(self.music_volume_number/10)
                    self.sm.Change_music_volume(new_volume)
            if self.minus_music_button.draw(self.screen):
                if(self.music_volume_number>0):
                    self.music_volume_number-=1
                    new_volume=float(self.music_volume_number/10)
                    self.sm.Change_music_volume(new_volume)
            self.draw_text(f"{self.music_volume_number}",self.screen.width/2-50,80)
            
            self.draw_text("SFX volume",self.screen.width/2-300,230)
            if self.plus_sfx_button.draw(self.screen):
                if(self.sfx_volume_number<10):
                    self.sfx_volume_number+=1
                    new_volume=float(self.sfx_volume_number/10)
                    self.sm.Change_sfx_volume(new_volume)
            if self.minus_sfx_button.draw(self.screen):
                if(self.sfx_volume_number>0):
                    self.sfx_volume_number-=1
                    new_volume=float(self.sfx_volume_number/10)
                    self.sm.Change_sfx_volume(new_volume)
            self.draw_text(f"{self.sfx_volume_number}",self.screen.width/2-50,310)

            if self.back_button.draw(self.screen):
                self.showing_options=False

class End_menu():
    #singleton code; creates a new instance if none exist, otherwise returns the instance
    def __new__(cls,screen,game_manager):
        if not hasattr(cls,'instance'):
            cls.instance=super().__new__(cls)
        return cls.instance
    
    def __init__(self,screen,game_manager):
        self.screen=screen
        self.font=pygame.font.SysFont("arialblack",60)
        self.text_colour=(0,0,0)
        self.music_volume_number=10
        self.sfx_volume_number=10
        self.game_manager=game_manager
        self.create_menu()
        self.sm=SoundManager()

    def create_menu(self):
        restart_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\restartbtn.png")
        self.restart_button=Button(300,self.screen.height-100,restart_btn_image, None,1)
        menu_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\mainmenubtn.png")
        self.menu_button=Button(self.screen.width-300,self.screen.height-100,menu_btn_image,None,1)
        
    def draw_text(self,text,x,y):
        img=self.font.render(text,True,self.text_colour)
        self.screen.blit(img,(x,y))

    def draw_menu(self,did_player_win):
            if did_player_win==True:
                self.draw_text(f"You Win!",self.screen.width/2-300,100)
            else:
                self.draw_text(f"You Lose...",self.screen.width/2-300,100)
            self.draw_text(f"Score: {self.game_manager.Score}",self.screen.width/2-300,230)
            if self.restart_button.draw(self.screen):
                return "restart"
            if self.menu_button.draw(self.screen):
                return "main_menu"
        
class Character_select_menu():
    #singleton code; creates a new instance if none exist, otherwise returns the instance
    def __new__(cls,screen):
        if not hasattr(cls,'instance'):
            cls.instance=super().__new__(cls)
        return cls.instance
    
    def __init__(self,screen):
        self.screen=screen
        self.font=pygame.font.SysFont("arialblack",60)
        self.text_colour=(0,0,0)
        self.music_volume_number=10
        self.sfx_volume_number=10
        self.create_menu()
        self.sm=SoundManager()
        self.character_chosen=None

    def create_menu(self):
        start_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\startbtn.png")
        self.start_button=Button(300,self.screen.height-100,start_btn_image,None,1)
        menu_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\mainmenubtn.png")
        self.menu_button=Button(self.screen.width-300,self.screen.height-100,menu_btn_image,None,1)
        echo_not_chosen_image=pygame.image.load(f"assets\\Images\\menuitems\\char choice echo.png")
        echo_chosen_image=pygame.image.load(f"assets\\Images\\menuitems\\char choice echo chosen.png")
        self.echo_button=Button(300,self.screen.height-400,echo_not_chosen_image,echo_chosen_image,2)
        emma_not_chosen_image=pygame.image.load(f"assets\\Images\\menuitems\\char choice emma.png")
        emma_chosen_image=pygame.image.load(f"assets\\Images\\menuitems\\char choice emma chosen.png")
        self.emma_button=Button(self.screen.width/2,self.screen.height-400,emma_not_chosen_image,emma_chosen_image,2)
        malthe_not_chosen_image=pygame.image.load(f"assets\\Images\\menuitems\\char choice malthe.png")
        malthe_chosen_image=pygame.image.load(f"assets\\Images\\menuitems\\char choice malthe chosen.png")
        self.malthe_button=Button(self.screen.width-300,self.screen.height-400,malthe_not_chosen_image,malthe_chosen_image,2)
        
    def draw_text(self,text,x,y):
        img=self.font.render(text,True,self.text_colour)
        self.screen.blit(img,(x,y))

    def draw_menu(self):
            if self.echo_button.draw(self.screen):
                self.echo_button.change_image(2)
                self.emma_button.change_image(1)
                self.malthe_button.change_image(1)
                self.character_chosen=True
            if self.emma_button.draw(self.screen):
                self.emma_button.change_image(2)
                self.echo_button.change_image(1)
                self.malthe_button.change_image(1)
                self.character_chosen=True
            if self.malthe_button.draw(self.screen):
                self.malthe_button.change_image(2)
                self.emma_button.change_image(1)
                self.echo_button.change_image(1)
                self.character_chosen=True
            if self.start_button.draw(self.screen) & (self.character_chosen is not None):
                return "start"
            if self.menu_button.draw(self.screen):
                return "main_menu"
            if self.echo_button.draw(self.screen):
                self.echo_button.change_image(2)

class Button():
    def __init__(self,x,y,image1,image2,scale):
        width=image1.get_width()
        height=image1.get_height()
        self.image=pygame.transform.scale(image1,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.clicked=False
        self.scale=scale
        self.image1=pygame.transform.scale(image1,(int(width*scale),int(height*scale)))
        if image2 is not None:
            self.image2=pygame.transform.scale(image2,(int(width*scale),int(height*scale)))
        self.position=(x,y)

    def change_image(self,number):
        if number==2:
            self.image=self.image2
        else:
            self.image=self.image1

    def draw(self,surface):
        action=False

        mouse_pos=pygame.mouse.get_pos()

        #check mouseover & clicked
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
        
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False

        surface.blit(self.image,(self.rect.x,self.rect.y))

        return action