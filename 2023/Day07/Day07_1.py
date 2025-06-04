from Hand import Hand

def main():
    hands_input: str = ''

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
