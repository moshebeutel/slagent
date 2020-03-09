
import World
import time


class Action(object):
    def __init__(self, name, world,inner_do, args ):
        self._name = name
        self._world = world
        self._termination = True
        self.__inner_do_func = inner_do
        self.__inner_do_params = args

    def precondition(self, state): 
        return True

    def termination(self, state):
        return self._termination
    
    def __inner_do(self):
        return self.__inner_do_func(self.__inner_do_params)

    def do(self, state):
        print ("Start Action  Name {}: {}".format(self._name, time.ctime())) 
        self._termination = False
        t = self.__inner_do()
        self._termination = True
        print ("End Action  Name {}: {}".format(self._name, time.ctime())) 
        next_state = state
        done = self._world.is_done(state=next_state)
        return next_state, done,  t