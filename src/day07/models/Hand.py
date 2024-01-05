from typing import List, Optional

from src.day07.models.Card import Card
from src.day07.models.HandRank import HandRank
from src.day07.models.Rank import Rank


class Hand:
    def __init__(self, rank_string, bid):
        self.cards: List[Card] = self.cards_from_rank_string(rank_string)

        if not isinstance(bid, int):
            bid = int(bid)
        self.bid = bid

        self.hand_rank = self.get_hand_rank()

    @staticmethod
    def cards_from_rank_string(rank_string):
        ranks = [Rank.from_short_name(rank) for rank in rank_string]
        return [Card(rank) for rank in ranks]

    def get_hand_rank(self):
        cards_in_hand = set(self.cards)
        rank_list = [card.rank for card in self.cards]
        rank_count = [rank_list.count(card.rank) for card in cards_in_hand]
        rank_count.sort(reverse=True)

        if rank_count[0] == 5:
            return HandRank.FIVE_OF_A_KIND
        elif rank_count[0] == 4:
            return HandRank.FOUR_OF_A_KIND
        elif rank_count[0] == 3 and rank_count[1] == 2:
            return HandRank.FULL_HOUSE
        elif rank_count[0] == 3:
            return HandRank.THREE_OF_A_KIND
        elif rank_count[0] == 2 and rank_count[1] == 2:
            return HandRank.TWO_PAIR
        elif rank_count[0] == 2:
            return HandRank.ONE_PAIR
        else:
            return HandRank.HIGH_CARD

    def __eq__(self, other):
        if not isinstance(other, Hand):
            raise NotImplementedError
        if self.hand_rank.value != self.hand_rank.value:
            return False
        for card_index in range(0, len(self.cards)):
            your_card: Card = self.cards[card_index]
            other_card: Card = other.cards[card_index]
            if your_card != other_card:
                return False
        return True

    def __lt__(self, other):
        if not isinstance(other, Hand):
            raise NotImplementedError
        if self.hand_rank.value < other.hand_rank.value:
            return True
        elif self.hand_rank.value > other.hand_rank.value:
            return False
        for card_index in range(0, len(self.cards)):
            your_card: Card = self.cards[card_index]
            other_card: Card = other.cards[card_index]
            if your_card < other_card:
                return True
            elif your_card > other_card:
                return False
        # equal in this case
        return False

    def __le__(self, other):
        if not isinstance(other, Hand):
            raise NotImplementedError
        if self.hand_rank.value < other.hand_rank.value:
            return True
        elif self.hand_rank.value > other.hand_rank.value:
            return False
        for card_index in range(0, len(self.cards)):
            your_card: Card = self.cards[card_index]
            other_card: Card = other.cards[card_index]
            if your_card < other_card:
                return True
            elif your_card > other_card:
                return False

        # equal in this case
        return True

    def __gt__(self, other):
        if not isinstance(other, Hand):
            raise NotImplementedError
        if self.hand_rank.value > other.hand_rank.value:
            return True
        elif self.hand_rank.value < other.hand_rank.value:
            return False
        for card_index in range(0, len(self.cards)):
            your_card: Card = self.cards[card_index]
            other_card: Card = other.cards[card_index]
            if your_card > other_card:
                return True
            elif your_card < other_card:
                return False

        # equal in this case
        return False

    def __ge__(self, other):
        if not isinstance(other, Hand):
            raise NotImplementedError
        if self.hand_rank.value > other.hand_rank.value:
            return True
        elif self.hand_rank.value < other.hand_rank.value:
            return False
        for card_index in range(0, len(self.cards)):
            your_card: Card = self.cards[card_index]
            other_card: Card = other.cards[card_index]
            if your_card > other_card:
                return True
            elif your_card < other_card:
                return False

        # equal in this case
        return True
