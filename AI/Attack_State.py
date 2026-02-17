from AI.State import State
from AI.AI_Conditions import AI_Conditions

class Attack_State(State):
    def __init__(self, obj, opponent):
        super().__init__(obj)
        self._opponent = opponent
        self._obj = obj

    def Execute(self, delta_time):
        
        distance = self._obj.transform.position[0] - self._opponent.transform.position[0]
        if distance > 150:
            self._obj.fsm.Set_Condition(AI_Conditions.Idle)

        return super().Execute()
    
    def Enter(self):
        return super().Enter()
    
    def Exit(self):
        return super().Exit()