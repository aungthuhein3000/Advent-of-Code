def main():
    file = open('input.txt')
    lines = file.readlines()

    all_matches = [] # number of matches for each card

    for line in lines:
        winning_numbers_str = line.strip().split(':')[1].split('|')[0].strip().split(' ')
        winning_numbers_int = [int(x) for x in winning_numbers_str if x.isdigit()]
        my_numbers_str = line.strip().split('|')[1].strip().split(' ')
        my_numbers_int = [int(x) for x in my_numbers_str if x.isdigit()]

        matches = 0 # count matches for each card
        for i in winning_numbers_int:
            if i in my_numbers_int:
                matches += 1
        all_matches.append(matches)
    
    num_cards = len(all_matches)
    cards = [1 for _ in range(num_cards)] # 1 copy for each card to start with

    total_cards = 0
    for i in range(num_cards - 1): # excluding last card to avoid indexing out of bounds
        for j in range(all_matches[i]):
            cards[i + j + 1] += cards[i]
        
        total_cards += cards[i]

    total_cards += cards[num_cards - 1] # add last card which does not make any copies

    print(total_cards)
    file.close()

if __name__ == '__main__':
    main()
