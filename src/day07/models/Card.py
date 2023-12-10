from src.day07.models.Rank import Rank


class Card:
    def __init__(self, rank):
        self.rank: Rank = rank

    def __hash__(self):
        return self.rank.value

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise NotImplementedError
        return self.rank.value == other.rank.value

    def __lt__(self, other):
        if not isinstance(other, Card):
            raise NotImplementedError
        return self.rank.value < other.rank.value

    def __le__(self, other):
        if not isinstance(other, Card):
            raise NotImplementedError
        return self.rank.value < other.rank.value

    def __gt__(self, other):
        if not isinstance(other, Card):
            raise NotImplementedError
        return self.rank.value < other.rank.value

    def __ge__(self, other):
        if not isinstance(other, Card):
            raise NotImplementedError
        return self.rank.value < other.rank.value

