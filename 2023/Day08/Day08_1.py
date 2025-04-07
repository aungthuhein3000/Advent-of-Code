# https://adventofcode.com/2023/day/8

def main():
    file = open(r"input.txt")

    directions: str = file.readline().strip() # list of directions to follow/repeat
    network: dict[str, tuple[str, str]] = {} # list of all tunnel "connections"
    direction_index: dict[str, int] = {'L': 0, 'R': 1} # to index into the tuple
    file.readline() # skip a line
    
    # load all tunnel connections to `network` dictionary
    for line in file:
        network[line[:3]] = line[7:10], line[12:15]
    file.close()

    current: str = 'AAA'
    steps: int = 0
    instruction_index: int = 0 # to index into `directions`
    while current != 'ZZZ':
        steps += 1

        # follow direction
        next_direction: str = directions[instruction_index] # get the next thing from 'LLRLRLRLR'
        current = network[current][direction_index[next_direction]]

        # loop around `directions`
        instruction_index += 1
        if instruction_index == len(directions):
            instruction_index = 0
        
    print(f"Total steps: {steps}") # answer: 13771


if __name__ == '__main__':
    main()
