
class policy():
    def __init__(self, action_space):
        assert isinstance(action_space, list) 
        self._actions = action_space
        self._num_of_actions = len(self._actions)
    
    def _get_action_logic(self, state):
        '''
        Pick action from action space according to policy
        Abstract Declaration
        '''
        raise NotImplementedError

    def get_action(self, state):
        idx = -1
        while idx < 0:
            idx = _get_action_logic(state)
            idx = -1 if not self._actions[idx].precondition(state) else idx 

        