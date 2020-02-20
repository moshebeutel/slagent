from policy import policy
import numpy as np

class RandomPolicy(policy):
    def get_action(self,state):
        idx = np.random.randint(self._num_of_actions)
        return self._actions[idx]