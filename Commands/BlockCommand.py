from Commands.Command import Command

class Block_command(Command):
    def __init__(self, player):
        super().__init__()
        self._player = player

    @property
    def blocking_filters(self):
        return ["crouch", "attack"]


    def Execute(self, is_repeated, delta_time):
        if (not is_repeated) & self.Pass_filter(self._player.input_filter):
            self._player.Block_toggle()

            # plays animation (moved Block_toggle)
            #self._player.asset_pack.Play_Block_Animation()

            # tells character that an action has been made
            self._player.Action_notification()

