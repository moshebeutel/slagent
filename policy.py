
class policy():
    def __init__(self, action_space):
        assert isinstance(action_space, list) 
        self._actions = action_space
        self._num_of_actions = len(self._actions)
    
    def get_action(self, state):
        raise NotImplementedError