import re

from src.day03.models.Coordinate import Coordinate
from src.day03.models.EngineSchematic import EngineSchematic
from src.day03.models.SchematicNumber import SchematicNumber
from src.day03.models.SchematicSymbol import SchematicSymbol
from src.utils.models.Line import Line


class GearRatiosLine(Line):

    def __init__(self, content, line_number):
        super().__init__(content)
        self.line_number = line_number
        self.content

    def match_schematic_numbers(self):
        pattern = r'(\d+)'
        return re.finditer(pattern, self.content)

    def match_schematic_symbols(self):
        pattern = r'[^.\d]'
        return re.finditer(pattern, self.content)

    def add_schematic_numbers_to_schematic(self, engine_schematic: EngineSchematic):
        matches = self.match_schematic_numbers()
        for match in matches:
            engine_schematic.add_schematic_number(
                SchematicNumber(
                    start_coord=Coordinate(row=self.line_number, col=match.start()),
                    # Note: minus 1 is because re gives you the index after the last match char
                    end_coord=Coordinate(row=self.line_number, col=match.end() - 1),
                    number=match.group()
                )
            )

    def add_schematic_symbols_to_schematic(self, engine_schematic: EngineSchematic):
        matches = self.match_schematic_symbols()
        for match in matches:
            engine_schematic.add_schematic_symbol(
                SchematicSymbol(
                    coordinate=Coordinate(row=self.line_number, col=match.start()),
                    symbol=match.group()
                )
            )
