from GameObject import GameObject
from abc import ABC

class Character(GameObject, ABC):

    def __init__(self):
        super.__init__()
        