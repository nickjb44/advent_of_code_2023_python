from typing import Set, List

from src.day03.models.Coordinate import Coordinate
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

    def add_schematic_number(self, schematic_number: SchematicNumber):
        self.schematic_numbers.append(schematic_number)

    def add_schematic_symbol(self, schematic_symbol: SchematicSymbol):
        self.schematic_symbols.add(schematic_symbol)
        self.coords_with_symbols.add(schematic_symbol.coordinate)

