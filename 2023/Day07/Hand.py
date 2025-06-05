"""
Represents a hand in a game of "Camel Cards".
"""

class Hand:
    __CARDS: dict[str, int] = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    def __init__(self, h: str) -> None:
        if len(h) != 5 or not all(c in Hand.__CARDS for c in h):
            raise ValueError(f'Error: "{h}" is not a valid hand')

        self.hand: str = h
        self.__card_counts: list[int] = self.__calcCardCounts() # counts of each card in desc order ('25252' => [3, 2])
        self.hand_type: str = self.__getHandType()

    def __calcCardCounts(self) -> list[int]:
        # could use collections.Counter here
        counts: dict[str, int] = {k: 0 for k in Hand.__CARDS.keys()}
        for card in self.hand:
            counts[card] += 1
        return sorted((x for x in counts.values() if x > 0), reverse = True)

    # This method assumes the card counts have been calculated already.
    def __getHandType(self) -> str:
        if self.__card_counts[0] == 5: # to avoid accessing index 1 below
            return 'Five of a Kind'

        match self.__card_counts[0], self.__card_counts[1]:
            case (4, _):
                return 'Four of a Kind'
            case (3, 2):
                return 'Full House'
            case (3, _):
                return 'Three of a Kind'
            case (2, 2):
                return 'Two Pairs'
            case (2, _):
                return 'One Pair'
            case (1, _):
                return 'High Card'
            case _:
                raise ValueError('Invalid hand type')

    def __lt__(self, other: 'Hand') -> bool:
        if len(self.__card_counts) == len(other.__card_counts):
            if self.__card_counts[0] != other.__card_counts[0]: # detect three of a kind and two pair
                return self.__card_counts[0] < other.__card_counts[0]

            for c1, c2 in zip(self.hand, other.hand):
                if c1 != c2:
                    return Hand.__CARDS[c1] < Hand.__CARDS[c2]
            return False
        else:
            return len(self.__card_counts) > len(other.__card_counts)

    def __eq__(self, other: object) -> bool: # pyright doesn't like `other: 'Hand'` here 🫤
        if not isinstance(other, Hand):
            raise TypeError("Comparison not supported between 'Hand' and other types.")
        return self.hand == other.hand

    def __repr__(self) -> str:
        return self.hand

