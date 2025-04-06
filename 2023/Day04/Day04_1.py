# https://adventofcode.com/2023/day/4

def main():
    file = open('input.txt')
    lines: list[str] = file.readlines()
    file.close()

    score: int = 0
    all_matches: list[int] = []

    for line in lines:
        winning_numbers_str: str = line.strip().split(':')[1].split('|')[0].strip().split(' ')
        winning_numbers_int: str = [int(x) for x in winning_numbers_str if x.isdigit()]
        my_numbers_str: str = line.strip().split('|')[1].strip().split(' ')
        my_numbers_int: int = [int(x) for x in my_numbers_str if x.isdigit()]

        matches: int = 0
        for i in winning_numbers_int:
            if i in my_numbers_int:
                matches += 1
        all_matches.append(matches)

    for match in all_matches:
        if match > 0:
            score += 2 ** (match - 1)

    print(f"Score: {score}") # Answer: 23678


if __name__ == '__main__':
    main()
