def main():
    file = open('input.txt')
    lines = file.readlines()

    score = 0
    all_matches = []

    for line in lines:
        winning_numbers_str = line.strip().split(':')[1].split('|')[0].strip().split(' ')
        winning_numbers_int = [int(x) for x in winning_numbers_str if x.isdigit()]
        my_numbers_str = line.strip().split('|')[1].strip().split(' ')
        my_numbers_int = [int(x) for x in my_numbers_str if x.isdigit()]

        matches = 0
        for i in winning_numbers_int:
            if i in my_numbers_int:
                matches += 1
        all_matches.append(matches)

    for match in all_matches:
        if match > 0:
            score += 2 ** (match - 1)

    print(f"Score: {score}")

    file.close()

if __name__ == '__main__':
    main()
