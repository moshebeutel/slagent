
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

        # backup actions
        actions_backup = self._actions.copy()
        
        while idx < 0 and len(self._actions) > 0:
            idx = self._get_action_logic(state)
            idx = -1 if not self._actions[idx].precondition(state) else idx 
            
            # do not choose the same action again if its preconditions are not met
            if idx < 0:
                self._actions.remove(idx)
        
        #restore actions
        if(len(self._actions) != len(actions_backup)):
            self._actions = actions_backup.copy()
        
        return self._actions[idx]