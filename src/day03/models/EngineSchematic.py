from typing import Set, List, Dict

from src.day03.models.Coordinate import Coordinate
from src.day03.models.Gear import Gear
from src.day03.models.SchematicNumber import SchematicNumber
from src.day03.models.SchematicSymbol import SchematicSymbol


class EngineSchematic:

    def __init__(self):
        '''
        I might regret this decision in part two
        but I'm gonna just store the relevant parts coordinates
        and ignore the whole graph and '.'s part.
        Will 100% be a mess if part 2 needs it...
        '''
        self.schematic_numbers: List[SchematicNumber] = []
        self.schematic_symbols: Set[SchematicSymbol] = set()
        self.coords_with_symbols: Set[Coordinate] = set()
        self.possible_gears: List[SchematicSymbol] = list()
        # this is super crufty, wouldn't scale, and I hate it but whatever
        # I don't want to do it in the schematic number so sticking with this
        self.coords_to_schematic_number: Dict[Coordinate, SchematicNumber] = {}

    def add_schematic_number(self, schematic_number: SchematicNumber):
        self.schematic_numbers.append(schematic_number)
        for col in range(schematic_number.start_coord.col, schematic_number.end_coord.col + 1):
            self.coords_to_schematic_number[Coordinate(schematic_number.start_coord.row, col)] = schematic_number


    def add_schematic_symbol(self, schematic_symbol: SchematicSymbol):
        self.schematic_symbols.add(schematic_symbol)
        self.coords_with_symbols.add(schematic_symbol.coordinate)
        if schematic_symbol.is_possible_gear():
            self.possible_gears.append(schematic_symbol)

    def get_gears(self):
        gears = []
        for possible_gear in self.possible_gears:
            schematic_number_neighbors = set()
            for row in range(possible_gear.coordinate.row - 1, possible_gear.coordinate.row + 2):
                for col in range(possible_gear.coordinate.col - 1, possible_gear.coordinate.col + 2):
                    coordinate = Coordinate(row=row, col=col)
                    if coordinate in self.coords_to_schematic_number:
                        # it's a set so it'll handle the duplicate number case automatically
                        # which is why I went through the trouble of implementing __add__ and __hash__
                        schematic_number_neighbors.add(self.coords_to_schematic_number[coordinate])
            if len(schematic_number_neighbors) == 2:
                gears.append(
                    Gear(*schematic_number_neighbors)
                )
        return gears



