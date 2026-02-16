from AI.State import State
from Enemy_States import Enemy_States

class FSM():
    def __init__(self, current_state, obj):
        self._current_state = current_state
        self._obj = obj

    def Execute(self):
        self._current_state.Execute()

    def Change_State(self, target_state):
        self._current_state.Exit()
        self._current_state = target_state
        self._current_state.Enter()