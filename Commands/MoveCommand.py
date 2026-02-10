import Commands.Command

class MoveCommand(Commands.Command):
    def __init__(self, player, direction):
        super().__init__()
        self._player = player
        self._direction = direction

    def Execute(self, direction):   
        self._player.transform.translate()
