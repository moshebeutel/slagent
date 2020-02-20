import numpy as np

class World(object):
    def __init__(self):
        print('world generated')
    def is_done(self, state):
        return np.random.rand( ) < 0.05 or np.random.rand() > 0.95