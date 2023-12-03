from src.day03.models.Coordinate import Coordinate


class SchematicNumber:
    def __init__(self, start_coord, end_coord, number):
        self.start_coord: Coordinate = start_coord
        self.end_coord: Coordinate = end_coord
        self.number = number

    def is_part_number(self, engine_schematic):
        return self.is_neighbor_to_symbol(engine_schematic)

    def is_neighbor_to_symbol(self, engine_schematic):
        """
        won't check for edge cases because I'm lazy but that's fine since there's
        not a real graph, we'll just never have a symbol in a negative index
        also needlessly checking the vals in the number chunk itself, not ideal
        but writing a get outer box coords method is a pain
        """
        for row_ind in range(self.start_coord.row - 1, self.start_coord.row + 2):
            for col_ind in range(self.start_coord.col - 1, self.end_coord.col + 2):
                neighbor_coord = Coordinate(row_ind, col_ind)
                if neighbor_coord in engine_schematic.coords_with_symbols:
                    return True

        return False

    def __add__(self, other):
        if isinstance(other, int):
            return int(self.number) + other
        return int(self.number) + int(other.number)

    def __radd__(self, other):
        if isinstance(other, int):
            return other + int(self.number)
        return int(self.number) + int(other.number)

    def __eq__(self, other):
        if not isinstance(SchematicNumber, other):
            raise NotImplementedError("only implemented for schematic numbers")
        return (
            self.number == other.number and
            self.start_coord == other.start_coord and
            self.end_coord == other.end_coord
        )

    def __hash__(self):
        return hash((self.number, self.start_coord, self.end_coord))

    def __mul__(self, other):
        if isinstance(other, int):
            return int(self.number) * other
        return int(self.number) * int(other.number)

    def __rmul__(self, other):
        if isinstance(other, int):
            return int(self.number) * other
        return int(self.number) * int(other.number)

