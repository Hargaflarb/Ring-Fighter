from GameObject import GameObject
from Characters.Player import Player
import pygame
from abc import ABC
from Components import Colider


class Void(GameObject):
    def __init__(self, game_world):
        super().__init__(game_world, pygame.math.Vector2(640, 720), 1)
        self.Add_component(Colider((1000,50,1000,0), 3))

        # saves the event trigger in a variable
        self.trigger_round_over = game_world.Make_event("Round_Over").Trigger


    def OnCollision(self, other):
        if other.__class__.__name__ == "Player":
            print("Player died.")
            self.game_world.game_objects_to_remove.append(other)

            # calls the methode that trigger the event
            self.trigger_round_over((2,))
        elif other.__class__.__name__ == "Enemy":
            # calls the methode that trigger the event
            self.trigger_round_over((1,))
            
            

    def Awake(self):
        # makes a lambda expression that is ran when the event is triggered (if you need multiple lines; use a methode)
        fn = lambda args: self.game_world.game_manager.End_round(args[0])

        # retrieves the event from the game world
        event = self.game_world.Get_event("Round_Over")

        # attaches the lambda expression to the event
        event.Subscribe(fn)
        
        # this can be done for any amount of lambda, methodes or functions, as long as they only take the one argument
        # the argument is a tuple that can store multiple or no arguments

