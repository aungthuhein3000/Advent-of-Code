# https://adventofcode.com/2023/day/8

import math

def findZ(network: dict[str, tuple[str, str]], directions: list[int], node: str) -> tuple[str, int]:
    INSTRUCTIONS: int = len(directions)
    steps: int = 0
    instruction_index: int = 0

    while True:
        node = network[node][directions[instruction_index]]
        steps += 1

        instruction_index += 1
        if instruction_index == INSTRUCTIONS:
            instruction_index = 0
        
        if node[2] == 'Z':
            break
    
        if steps > 10_000_000: # Arbitrary. This is why this has to be an assumption. (Although you could write code to check this too.)
            raise ValueError('Error: exceeded 10 million steps while trying to find Z')

    return node, steps

def verify_assumptions(network: dict[str, tuple[str, str]], directions: list[int]) -> None:
    """
    To verify assumptions about the problem:
    - check if all nodes are going in a loop
    - check if # of steps for the loop is divisible by # of instructions
    """

    print("Checking assumptions...")

    starting_nodes: list[str] = [x for x in network.keys() if x[2] == 'A'] # list of nodes to keep track of
    NODES: int = len(starting_nodes) # number of nodes to follow simultaneously
    ending_nodes: list[str] = ['' for _ in range(NODES)] # first Z found
    ending_nodes_2: list[str] = ['' for _ in range(NODES)] # end after looking for a loop
    steps_to_reach_Z: list[int] = [0 for _ in range(NODES)] # keep track of number steps for each node
    steps_to_loop: list[int] = [0 for _ in range(NODES)]

    # traverse the network for each node INDEPENDENTLY
    for i in range(NODES):
        # find the first Z
        ending_nodes[i], steps_to_reach_Z[i] = findZ(network, directions, starting_nodes[i])
        # find another Z to see if it loops around
        ending_nodes_2[i], steps_to_loop[i] = findZ(network, directions, ending_nodes[i])
    
    # print a report
    print(f'# of starting nodes: {NODES}')
    print(f'Starting nodes: {starting_nodes}')
    print(f'Ending nodes: {ending_nodes}')
    print(f'Steps taken to reach Z: {steps_to_reach_Z}')
    print(f'Ending nodes (2nd Z): {ending_nodes_2}')
    print(f'Steps to reach 2nd Z: {steps_to_loop}')

    # check
    INSTRUCTIONS = len(directions) # number of directions in the first line of input 
    end_in_loop: bool = True # check if # of steps is divisible by INSTRUCTIONS
    for i in range(NODES):
        if ending_nodes[i] != ending_nodes_2[i] or steps_to_loop[i] % INSTRUCTIONS != 0:
            end_in_loop = False
            break
    
    if end_in_loop:
        print('Successful! All paths end in a loop.')
    else:
        raise ValueError('Error: assertions failed')


def main() -> int:
    file = open(r"/Users/aungthuhein/Documents/My documents/Code/My repos/Advent-of-Code/2023/Day08/input.txt")
    directions: list[int] = [int(x == 'R') for x in file.readline().strip()] # list of directions to follow/repeat. 0 for left, 1 for right
    network: dict[str, tuple[str, str]] = {} # list of all tunnel "connections"

    # load all tunnel connections to `network` dictionary
    file.readline() # skip a line
    for line in file:
        network[line[0:3]] = line[7:10], line[12:15]
    file.close() # done with the file

    try:
        verify_assumptions(network, directions)
    except ValueError as ve:
        print(ve)
        return 1
    
    current: list[str] = [node for node in network.keys() if node[2] == 'A']
    NODES: int = len(current)
    steps: list[int] = [0 for _ in range(NODES)]
    for i in range(NODES):
        _, steps[i] = findZ(network, directions, current[i])

    print(f"\nTotal steps: {math.lcm(*steps):,}") # answer: 13,129,439,557,681
    return 0


if __name__ == '__main__':
    main()
