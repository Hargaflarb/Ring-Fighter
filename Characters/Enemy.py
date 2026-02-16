from GameObject import GameObject
import Components
import pygame

class Enemy(GameObject):
    def __init__(self, game_world, position, scale, difficulty):
        super().__init__(game_world, position, scale)

        speed = 50
        sr = self.Add_component(Components.SpriteRenderer("temp playercharacter.png"))
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(), sr.sprite_image.get_height())

        self.Add_component(Components.Momentum())
        self.Add_component(Components.Gravity())
        self.Add_component(Components.Colider((self._sprite_size[0]/2,self._sprite_size[1],self._sprite_size[0]/2,0), 2))

        if difficulty == "Easy":
            print("Easy")
        elif difficulty == "Normal":
            print("Normal")
        elif difficulty == "Boss":
            print("Boss")
        
    def Move(self, direction, delta_time):
        if direction != pygame.math.Vector2(0, 0):
           direction.normalize
        change = ((direction * self.speed))
        self.transform.translate(change*delta_time)


