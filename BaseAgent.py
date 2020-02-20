from Action import Action as action
import numpy as np

class BaseAgent(action):
    """
    Base class for all agents Atomic or High level, learning or planning
    """
    def __init__(self, policy):
        self._currentActionInProcess = None
        self._policy = policy

    def do(self, state):   
        next_state, done, elapsed_time = self._currentActionInProcess.step(state) if isinstance(self._currentActionInProcess, BaseAgent) else self._currentActionInProcess.do(state)

        return next_state, done, elapsed_time

    def step(self, worldState):
        self._worldState = worldState
        step_done = False
        step_time = 0
        done = False
        while(not step_done and not done):
            self._currentActionInProcess = self._policy.get_action(self._worldState)
            next_state, done, elapsed_time = self.do(worldState)
            step_time += elapsed_time
            step_done = np.random.randint(0,10) > 7
        


        return next_state, done, step_time



    


