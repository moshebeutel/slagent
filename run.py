from CompoundAgent import CompoundAgent as ca
import policy
import argparse
from AtomicAgent import AtomicAgent as aa
from policy import policy as policy

def build_hierarchy():
    """
    builder function  - builds agent hierarchy
    """

    p1 = policy
    p2 = policy
    p3 = policy

    grabStoneAgent = aa(p1)
    moveToAgent = aa(p2)
    grabAndMoveAgent = ca(p3, [grabStoneAgent, moveToAgent])
    return grabAndMoveAgent

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                 help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                 const=sum, default=max,
    #                 help='sum the integers (default: find the max)')

    args = parser.parse_args()
    # print(args.accumulate(args.integers))
  
    high_level_agent = build_hierarchy()

    print(high_level_agent)

    

if __name__== "__main__":
  main()