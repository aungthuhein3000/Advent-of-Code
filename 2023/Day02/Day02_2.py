def main():
    file_input = open('/Users/aungthuhein/Documents/My Documents/Code/Advent of Code/2023/Day02/input.txt')
    lines = file_input.readlines()

    # Example line below:
    # Game 15: 4 green, 12 blue, 15 red; 10 blue, 18 green, 13 red; 20 blue, 6 green, 10 red; 20 red, 12 blue, 13 green; 12 blue, 17 green, 10 red; 1 red, 3 blue, 7 green
    total: int = 0
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    for line in lines:

        # error checking here maybe ...

        rolls = line.split(':')[1].split(';') # ["1 red, 2 green, 8 blue", "4 green, 2 red"]
        for roll in rolls: # " 1 red, 2 green, 8 blue"
            colors = roll.split(',') # [" 1 red", " 2 green", " 8 blue"]
            for color in colors: # " 1 red"
                parts = color.strip().split(' ') # ["1", "red"]
                if int(parts[0]) > max_cubes[parts[1]]:
                    max_cubes[parts[1]] = int(parts[0])
        
        total += max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]

        for key in max_cubes.keys():
            max_cubes[key] = 0

        # print(line.strip())
        # print(f"Game {game_id} is valid")
        # input("Press Enter to continue... ")
        # print()
    
    print(total)
    


if __name__ == '__main__':
    main()
