def main():
    with open('input.txt') as file:
        seeds: list[int] = [int(x) for x in file.readline().strip().split() if x.isdigit()]
        file.readline() # skip blank line 2

        for _ in range(7):
            file.readline() # skip a line
            
            destination: list[int] = []
            source: list[int] = []
            range_length: list[int] = []

            # read the numbers
            while True:
                line: str = file.readline()
                if line.strip() == '':
                    break
                entry: list[int] = [int(x) for x in line.split()]
                destination.append(entry[0])
                source.append(entry[1])
                range_length.append(entry[2])
            
            # map the seeds
            for s in range(len(seeds)):
                for m in range(len(destination)): # for each mapping
                    if seeds[s] >= source[m] and seeds[s] < source[m] + range_length[m]:
                        seeds[s] = seeds[s] - source[m] + destination[m]
                        break # Found mapping for seed. Break.
                
        print(f'Locations: {seeds}')
        print(f'Min: {min(seeds)}')

if __name__ == '__main__':
    main()