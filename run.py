from RandomPolicy import RandomPolicy
import argparse
from Action import Action as action
from BaseAgent import BaseAgent as Agent
import World
import time
import numpy as np
def sleep_some(args):
    assert len(args) == 2
    avg_duration, std_duration = args[0], args[1]
    t = np.random.normal(avg_duration, std_duration) 
    time.sleep( t )
    return t

def build_hierarchy():
    """
    builder function  - builds agent hierarchy
    """
    world = World.World()
    action_space = [action('action' + str(i), world, sleep_some,  (i / 10.0 ,  1 / (20.0 * (i + 1))))  for i in range(20)]
    # action_space = [action(name = 'action' + str(i), world=world, inner_do = sleep_some,  average_duration = i / 10.0 , std_duration = 1 / (20.0 * (i + 1)))  for i in range(20)]
    grab_stone_policy = RandomPolicy(action_space[:10])
    navigation_policy = RandomPolicy(action_space[11:20])
    grab_stone_agent = Agent(grab_stone_policy)
    moveToAgent = Agent(navigation_policy)
    high_level_policy = RandomPolicy([grab_stone_agent, moveToAgent])
    grabAndMoveAgent = Agent(high_level_policy)
    return grabAndMoveAgent

def main_loop(root_agent):
    '''
    Run High Level agent in Enviornment untill done
    '''

    done = False
    state = [1,2]
    while(not done):
        state, done, elapsed_time =  root_agent.step(state)
        print('root agent state', state, 'done', done, 'elapsed time', elapsed_time)

def main():
    high_level_agent = build_hierarchy()
    print(high_level_agent)
    main_loop(high_level_agent)



if __name__== "__main__":
  main()