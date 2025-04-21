import sys

def fill_gaps(mappings: list[list[int]]) -> None: # will modify `mappings`
    i: int = 1 # start index at 1
    while i < len(mappings):
        if mappings[i][1] != mappings[i - 1][2] + 1:
            mappings.insert(i, [
                mappings[i - 1][2] + 1,
                mappings[i - 1][2] + 1,
                mappings[i][1] - 1
            ])
            i += 1
        i += 1
    
    # add a line for max (9,223,372,036,854,775,807)
    if mappings[-1][2] < sys.maxsize:
        mappings.append([mappings[-1][2] + 1, mappings[-1][2] + 1, sys.maxsize])
    
    # add a line starting at 0
    for m in mappings:
        if m[0] == 0:
            return
    mappings.insert(0, [0, 0, mappings[0][1] - 1])

def main():
    """
    assumes:
        - every section has a range starting at 0
        - no seeds are less than 0
    """
    with open('input.txt') as file:
        seeds_and_steps: list[int] = [int(x) for x in file.readline().strip().split() if x.isdigit()]
        file.readline() # skip blank line after
        seeds: list[tuple[int, int]] = []
        for i in range(0, len(seeds_and_steps), 2):
            seeds.append((seeds_and_steps[i], seeds_and_steps[i] + seeds_and_steps[i + 1] - 1)) # tuple of (start, end)
        
        for _ in range(7):
            # 1. read lines
            file.readline() # skip the "seed-to-soil map:" line
            mappings: list[list[int]] = [] # list of [destination, source, steps]

            while True:
                line: str = file.readline().strip()
                if not line:
                    break
                strings: list[str] = line.split()
                mappings.append([
                    int(strings[0]), # destination
                    int(strings[1]), # start
                    int(strings[1]) + int(strings[2]) - 1 # end as opposed to steps
                ])
                
            # 2. sort 
            mappings.sort(key = lambda a: a[1]) # sort by source (start)

            # 3. fill gaps
            fill_gaps(mappings) # will modify `mappings`

            # 4. create maps
            new_seeds: list[tuple[int, int]] = []
            for seed in seeds: # go through seeds
                for i in range(len(mappings) - 1, -1, -1): # go through mappings in reverse.
                    if mappings[i][1] <= seed[0]: # if starting point found
                        if seed[1] <= mappings[i][2]: # if ending point is also in the same range as starting point
                            new_seeds.append((
                                seed[0] - mappings[i][1] + mappings[i][0],
                                seed[1] - mappings[i][1] + mappings[i][0] ))
                            break # Done with current seed. Move on to another seed.
                        else: # ending point goes beyond current range in mappings
                            new_seeds.append((
                                seed[0] - mappings[i][1] + mappings[i][0],
                                mappings[i][2] - mappings[i][1] + mappings[i][0] ))

                            j: int = i + 1
                            while True:
                                if seed[1] <= mappings[j][2]:
                                    new_seeds.append((
                                        mappings[j][0],
                                        seed[1] - mappings[j][1] + mappings[j][0] ))
                                    break
                                else:
                                    new_seeds.append((
                                        mappings[j][0],
                                        mappings[j][2] - mappings[j][1] + mappings[j][0]))
                                    j += 1
                            break # Done with current seed.

            seeds = new_seeds
    
    print(f'Lowest location number: {min(seeds)[0]}')


if __name__ == '__main__':
    main()
