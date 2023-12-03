from enum import Enum


class Cube:

    def __init__(self, color, count):
        self.color = color
        self.count = count


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
