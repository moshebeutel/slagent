class BaseAgent():
    """
    Base class for all agents Atomic or High level, learning or planning
    """
    def __init__(self, policy):
        self._currentActionInProcess = None
        self._policy = policy

    def step(self, worldState):
        self._worldState = worldState
        self._currentActionInProcess = self._policy.get_action(self._worldState)
        return self._currentActionInProcess   #, estimatedTimeLeft



    


