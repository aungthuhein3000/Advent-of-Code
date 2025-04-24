# could use this too:
# from collections import Counter
# specifically Counter.most_common()

class Hand:
    __CARDS: dict[str, int] = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    def __init__(self, h: str) -> None:
        if len(h) != 5 or [c for c in h if c not in Hand.__CARDS.keys()] != []:
            raise ValueError(f'Error: "{h}" is not a valid hand')
        self.hand: str = h
        self.__card_counts: list[int] = self.__calcCardCounts() # counts of each card in desc order ('25252' => [3, 2])
        self.hand_type: str = self.__getHandType()

    def __calcCardCounts(self) -> list[int]:
        __card_counts: dict[str, int] = {k: 0 for k in Hand.__CARDS.keys()}
        for card in self.hand:
            __card_counts[card] += 1
        return sorted([x for x in __card_counts.values() if x > 0], reverse = True)

    def __getHandType(self) -> str:
        if self.__card_counts[0] == 5:
            return 'Five of a Kind'
        elif self.__card_counts[0] == 4:
            return 'Four of a Kind'
        elif self.__card_counts[0] == 3: # [3, 2] or [3, 1, 1]
            if self.__card_counts[1] == 2: # [3, 2]
                return 'Full House'
            else: # [3, 1, 1]
                return 'Three of a Kind'
        elif self.__card_counts[0] == 2: # [2, 2, 1] or [2, 1, 1, 1]
            if self.__card_counts[1] == 2:
                return 'Two Pair'
            else:
                return 'One Pair'
        else:
            return 'High Card'

    def __lt__(self, other: 'Hand') -> bool: # why can't I do `other: Hand` here?
        if len(self.__card_counts) == len(other.__card_counts):
            for c1, c2 in zip(self.hand, other.hand):
                if c1 != c2:
                    return Hand.__CARDS[c1] < Hand.__CARDS[c2]
            return False
        else:
            return len(self.__card_counts) > len(other.__card_counts)

    def __eq__(self, other: 'Hand') -> bool:
        return self.hand == other.hand

    def __str__(self):
        return self.hand
