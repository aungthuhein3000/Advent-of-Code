"""
Represents a hand in a game of "Camel Cards".
"""

class Hand:
    # static members
    CARDS: dict[str, int] = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    JOKER: str = 'J'
    HAND_SIZE: int = 5


    @staticmethod
    def __getCardCounts(hand: str) -> list[tuple[int, str]]:
        # could use collections.Counter here
        counts: dict[str, int] = {}
        for card in hand:
            if card in counts:
                counts[card] += 1
            else:
                counts[card] = 1
        return sorted(((count, card) for card, count in counts.items()), reverse = True)
        # unnecessary to sort by `card` as well here


    @staticmethod
    def __getBestCard(hand: str) -> str: # hand with no jokers
        if len(hand) == 1:
            return hand

        return Hand.__getCardCounts(hand)[0][1]


    @staticmethod
    def __getBestHand(hand: str) -> str: # hand with jokers
        if Hand.JOKER not in hand or hand == Hand.JOKER * Hand.HAND_SIZE:
            return hand
        else:
            best_card: str = Hand.__getBestCard(hand.replace(Hand.JOKER, ''))
            return hand.replace(Hand.JOKER, best_card)
    # end of static members


    def __init__(self, hand: str) -> None:
        if len(hand) != 5 or not all(c in Hand.CARDS for c in hand):
            raise ValueError(f'Error: "{h}" is not a valid hand')

        self.hand: str = hand
        best_hand: str = Hand.__getBestHand(hand) # jokers converted to make best hand
        self.__card_counts: list[tuple[int, str]] = Hand.__getCardCounts(best_hand) # counts of each card in desc order ('25252' => [3, 2])


    # This method assumes the card counts have been calculated already.
    def __getHandType(self) -> str:
        if self.__card_counts[0][0] == 5: # to avoid accessing index 1 below
            return 'Five of a Kind'

        match self.__card_counts[0][0], self.__card_counts[1][0]:
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


    """
     Five of a Kind: [(5, _)]
     Four of a Kind: [(4, _), (1, _)]
         Full House: [(3, _), (2, _)]
    Three of a Kind: [(3, _), (1, _), (1, _)]    <--- same length
          Two Pairs: [(2, _), (2, _), (1, _)]    <--- same length
           One Pair: [(2, _), (1, _), (1, _), (1, _)]
          High Card: [(1, _), (1, _), (1, _), (1, _), (1, _)]
    """
    def __lt__(self, other: 'Hand') -> bool:
        if len(self.__card_counts) == len(other.__card_counts):
            if self.__card_counts[0][0] != other.__card_counts[0][0]: # detect three of a kind and two pairs
                return self.__card_counts[0][0] < other.__card_counts[0][0]

            for c1, c2 in zip(self.hand, other.hand): # compare normal hands including jokers
                if c1 != c2:
                    return Hand.CARDS[c1] < Hand.CARDS[c2]
            return False
        else:
            return len(self.__card_counts) > len(other.__card_counts)


    def __eq__(self, other: object) -> bool: # pyright doesn't like `other: 'Hand'` here 🫤
        if not isinstance(other, Hand):
            raise TypeError("Comparison not supported between 'Hand' and other types.")
        return self.hand == other.hand


    def __str__(self) -> str:
        return f"{self.hand} ({self.__getHandType()})"


    def __repr__(self) -> str:
        return self.hand

