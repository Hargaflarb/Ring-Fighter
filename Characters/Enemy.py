from GameObject import GameObject
import Components


class Enemy(GameObject):
    def __init__(self, game_world, position, scale):
        super().__init__(game_world, position, scale)

        speed = 50
        sr = self.Add_component(Components.SpriteRenderer("temp playercharacter.png"))
        input_handler = self.Add_component(Components.Input_Handler(self))

