from typing import List

from src.day03.models.EngineSchematic import EngineSchematic
from src.day03.models.Gear import Gear
from src.day03.models.GearRatiosLine import GearRatiosLine


def read_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def set_up_engine_schematic(lines):
    engine_schematic = EngineSchematic()
    # could maybe do it in map probably but easier for me to think this way
    for line_number, line in enumerate(lines):
        gear_ratios_line = GearRatiosLine(line_number=line_number, content=line)

        # maybe I should've put these in the engine not the line? idk
        gear_ratios_line.add_schematic_numbers_to_schematic(engine_schematic)
        gear_ratios_line.add_schematic_symbols_to_schematic(engine_schematic)
    return engine_schematic


def calculate_sum_of_gear_ratios(lines):
    engine_schematic: EngineSchematic = set_up_engine_schematic(lines)

    gears: List[Gear] = engine_schematic.get_gears()

    return sum([gear.calculate_gear_ratio() for gear in gears])


def main(file_path):
    sum_of_gear_ratios = calculate_sum_of_gear_ratios(
        read_lines(file_path)
    )

    print(f"the sum of gear ratios is {sum_of_gear_ratios}")
    return sum_of_gear_ratios


if __name__ == "__main__":
    file_path = "input/input.txt"
    main(file_path)
