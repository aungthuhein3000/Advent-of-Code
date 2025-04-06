def main():
    file_input = open(r'input.txt')
    lines: list[str] = file_input.readlines()

    # Example line below:
    # Game 15: 4 green, 12 blue, 15 red; 10 blue, 18 green, 13 red; 20 blue, 6 green, 10 red; 20 red, 12 blue, 13 green; 12 blue, 17 green, 10 red; 1 red, 3 blue, 7 green
    max_cubes: dict[str, int] = {"red": 12, "green": 13, "blue": 14}
    game_id_total: int = 0

    for line in lines:
        rolls: list[str] = line.split(':')[1].split(';') # ["1 red, 2 green, 8 blue", "4 green, 2 red"]
        valid_game: bool = True
        # roll_index: int = 0
        for roll in rolls: # " 1 red, 2 green, 8 blue"
            colors: list[str] = roll.split(',') # [" 1 red", " 2 green", " 8 blue"]
            for color in colors: # " 1 red"
                parts: list[str] = color.strip().split(' ') # ["1", "red"]
                if int(parts[0]) > max_cubes[parts[1]]:
                    valid_game = False
                    break

            if not valid_game:
                break
        
        if valid_game:
            game_id: int = int(line.split(':')[0].split(' ')[1])
            game_id_total += game_id

    print(f"ID total: {game_id_total}") # answer: 2348

    file_input.close()


if __name__ == '__main__':
    main()
