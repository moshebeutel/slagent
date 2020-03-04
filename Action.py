import time
import numpy as np
import World

class Action(object):
    def __init__(self, name, world, average_duration = 10000, std_duration = 0 ):
        self._name = name
        self._world = world
        

    def precondition(self, state): 
        return True

    
    def termination(self, state):
        raise NotImplementedError
    
    def do(self, state):
        print ("Start Action  Name {}: {}".format(self._name, time.ctime())) 
        t = np.random.normal(self._avg_duration, self._std_duration)
        time.sleep( t )
        print ("End Action  Name {}: {}".format(self._name, time.ctime())) 
        next_state = state
        done = self._world.is_done(state=next_state)
        return next_state, done,  t