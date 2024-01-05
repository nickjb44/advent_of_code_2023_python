from enum import Enum


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    @classmethod
    def from_short_name(cls, name):
        short_name_to_rank_map = {
            '2': cls.TWO, '3': cls.THREE, '4': cls.FOUR,
            '5': cls.FIVE, '6': cls.SIX, '7': cls.SEVEN,
            '8': cls.EIGHT, '9': cls.NINE, 'T': cls.TEN,
            'J': cls.JACK, 'Q': cls.QUEEN, 'K': cls.KING, 'A': cls.ACE
        }
        if name not in short_name_to_rank_map:
            raise ValueError(f'rank {name} not found in the map, check your input')
        return short_name_to_rank_map[name]


