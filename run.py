from CompoundAgent import CompoundAgent
from RandomPolicy import RandomPolicy
import argparse
from AtomicAgent import AtomicAgent
from Action import Action as action
from BaseAgent import BaseAgent as base_agent
import World

def build_hierarchy():
    """
    builder function  - builds agent hierarchy
    """
    world = World.World()
    action_space = [action(name = 'action' + str(i), world=world, average_duration = i / 10.0 , std_duration = 1 / (20.0 * (i + 1)))  for i in range(20)]
    p1 = RandomPolicy(action_space[:10])
    p2 = RandomPolicy(action_space[11:20])
    grabStoneAgent = base_agent(p1)
    moveToAgent = base_agent(p2)
    p3 = RandomPolicy([grabStoneAgent, moveToAgent])
    grabAndMoveAgent = base_agent(p3)
    return grabAndMoveAgent

def main_loop(root_agent):
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