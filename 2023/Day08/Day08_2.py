# https://adventofcode.com/2023/day/8

def main():
    file = open(r"test_input_2.txt")
    # list of directions to follow/repeat. 0 for left, 1 for right
    directions: list[int] = [int(x == 'R') for x in file.readline().strip()]
    instruction_count: int = len(directions) 

    network: dict[str, tuple[str, str]] = {} # list of all tunnel "connections"
    file.readline() # skip a line
    
    # load all tunnel connections to `network` dictionary
    for line in file:
        network[line[0:3]] = line[7:10], line[12:15]
    file.close() # done with the file

    # find starting nodes
    current: list[str] = [x for x in network.keys() if x[2] == 'A'] # list of nodes to keep track of
    nodes: int = len(current) # number of nodes to follow simultaneously

    instruction_index: int = 0

    steps: int = 0
    end_reached: bool = False
    while not end_reached:
        steps += 1

        # follow each node
        for i in range(nodes):
            current[i] = network[current[i]][directions[instruction_index]]

        # loop around `directions`
        # could also just do instruction_index %= instruction_count, but this might be faster
        instruction_index += 1
        if instruction_index == instruction_count:
            instruction_index = 0

        # debug message
        if steps % 10_000_000 == 0:
            print(f'{steps:,}')
        
        # check if end is reached
        end_reached: bool = True
        for i in range(nodes):
            if current[i][2] != 'Z':
                end_reached = False
                break # break out of for loop only

    print(f"Total steps: {steps}") # answer: 


if __name__ == '__main__':
    main()
