from enum import Enum


class HandRank(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5  # not used (yet?)
    FLUSH = 6  # not used (yet?)
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    FIVE_OF_A_KIND = 9
    STRAIGHT_FLUSH = 10  # not used (yet?)
    ROYAL_FLUSH = 11  # not used (yet?)


