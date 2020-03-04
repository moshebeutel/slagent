from RandomPolicy import RandomPolicy
import argparse
from Action import Action as action
from BaseAgent import BaseAgent as Agent
import World

def build_hierarchy():
    """
    builder function  - builds agent hierarchy
    """
    world = World.World()
    action_space = [action(name = 'action' + str(i), world=world, average_duration = i / 10.0 , std_duration = 1 / (20.0 * (i + 1)))  for i in range(20)]
    grab_stone_policy = RandomPolicy(action_space[:10])
    navigation_policy = RandomPolicy(action_space[11:20])
    grabStoneAgent = Agent(grab_stone_policy)
    moveToAgent = Agent(navigation_policy)
    high_level_policy = RandomPolicy([grabStoneAgent, moveToAgent])
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