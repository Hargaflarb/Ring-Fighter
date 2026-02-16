import pygame

class Start_menu:
    def __init__(self,screen):
        self.screen=screen
        self.font=pygame.font.SysFont("arialblack",40)
        self.text_colour=(0,0,0)
        self.create_menu()

    def create_menu(self):
        start_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\startbtn.png")
        self.start_button=Button(self.screen.width/2,150,start_btn_image,1)
        options_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\optionsbtn.png")
        self.options_button=Button(self.screen.width/2,300,options_btn_image,1)
        quit_btn_image=pygame.image.load(f"assets\\Images\\menuitems\\quitbtn.png")
        self.quit_button=Button(self.screen.width/2,450,quit_btn_image,1)
        
    def draw_menu(self):
        self.start_button.draw(self.screen)
        self.options_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        
    def draw_text(self,text,x,y):
        img=self.font.render(text,True,self.text_colour)
        self.screen.blit(img,(x,y))
    
class Button():
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.clicked=False

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