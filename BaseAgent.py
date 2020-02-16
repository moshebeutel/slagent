class BaseAgeny():
    """
    Base class for all agents Atomic and High level, learning and planning
    """
    def __init__(self, children):
        isAtomic = children == None or len(children)
        self._children = None if isAtomic == True else children
        self._isAtomic = isAtomic 
        self._currentActionInProcess = None
    
    def _get_action(self):
        raise NotImplementedError

    def step(self, worldState):
        self._worldState = worldState
        return action, estimatedTimeLeft

