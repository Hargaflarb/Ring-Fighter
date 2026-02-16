from Commands.Command import Command

class Multi_command(Command):
    def __init__(self, first_command, second_command, condition_call):
        super().__init__()
        self._first_command = first_command
        self._second_command = second_command
        self._condition = condition_call # runs first command if true, runs second command if false
    
    def Execute(self, is_repeated, delta_time):
        if self._condition():
            self._first_command.Execute(is_repeated, delta_time)
        else:
            self._second_command.Execute(is_repeated, delta_time)