from Handv2 import Hand

def read_file(file_name: str) -> list[tuple[Hand, int]]:
    with open(file_name) as file:
        hands: list[tuple[Hand, int]] = []
        while line := file.readline():
            hand_and_bet: list[str] = line.split()
            if len(hand_and_bet) != 2:
                break

            try:
                bet_amount: int = int(hand_and_bet[1])
            except ValueError as ve:
                print(f'Error: {ve}')
            else:
                hands.append((Hand(hand_and_bet[0]), bet_amount))

        return hands


def main() -> None:
    hands: list[tuple[Hand, int]] = read_file('input.txt')
    hands.sort(key = lambda x: x[0])

    total_winnings: int = 0
    for rank in range(1, len(hands) + 1):
        total_winnings += rank * hands[rank - 1][1]

    print(f"Total winnings: {total_winnings}")


def test_Hand() -> None:
    """
    For testing the Hand class.
    """
    while hands_input := input("Enter your hands: "):
        hands: list[str] = hands_input.split()
        if len(hands) != 2:
            print('Please provide two hands.\n')
            continue

        try:
            h1 = Hand(hands[0])
            h2 = Hand(hands[1])
        except ValueError as ve:
            print(f'{ve}.\n')
        else:
            if h1 < h2:
                print(f'{h1} ({h1.hand_type}) < {h2} ({h2.hand_type})')
            elif h1 == h2:
                print(f'{h1} ({h1.hand_type}) == {h2} ({h2.hand_type})')
            else:
                print(f'{h1} ({h1.hand_type}) > {h2} ({h2.hand_type})')
            print()

    print('Exiting...')

if __name__ == '__main__':
    main()
    # test_Hand()
