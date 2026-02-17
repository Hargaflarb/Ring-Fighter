from AI.State import State
from Components import Component
from AI.AI_Conditions import AI_Conditions

class FSM(Component):
    def __init__(self, current_state, obj):
        self._current_state = current_state
        self._current_condition = AI_Conditions.Null
        self._obj = obj
        self._transitions = {}

    def Update(self, delta_time):
        self.Process_Transitions()
        self._current_condition = AI_Conditions.Null
        if self._current_state is not None:
            self._current_state.Execute(delta_time)
    
    def Set_Condition(self, condition):
        self._current_condition = condition

    def Add_Transition(self, from_state, condition, to_state):
        self._transitions[(from_state, condition)] = to_state

    def Process_Transitions(self):
        if self._transitions.get((type(self._current_state), self._current_condition)) is not None:
            value = self._transitions[(type(self._current_state), self._current_condition)]
            self.Change_State(value)
        

    def Change_State(self, target_state):
        if self._current_state is None:
            self._current_state.Exit()
        self._current_state = target_state
        self._current_state.Enter()

    def Awake(self,game_world):
        pass
    
    def Start(self):
        pass

