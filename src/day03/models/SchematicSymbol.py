from src.day03.models.Coordinate import Coordinate


class SchematicSymbol:
    def __init__(self, coordinate, symbol):
        self.coordinate: Coordinate = coordinate
        if symbol == '\n':
            raise ValueError("PANIC! This should have been sanitized")
        self.symbol = symbol

    def is_possible_gear(self):
        return self.symbol == "*"
