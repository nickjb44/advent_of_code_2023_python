from functools import reduce

from src.day03.models.EngineSchematic import EngineSchematic
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


def calculate_sum_of_part_numbers(lines):
    engine_schematic: EngineSchematic = set_up_engine_schematic(lines)

    part_numbers = filter(
        lambda schematic_number: schematic_number.is_part_number(engine_schematic),
        engine_schematic.schematic_numbers
    )

    return sum(list(part_numbers))


def main(file_path):
    sum_of_part_numbers = calculate_sum_of_part_numbers(
        read_lines(file_path)
    )

    print(f"the sum of part numbers is {sum_of_part_numbers}")
    return sum_of_part_numbers


if __name__ == "__main__":
    file_path = "input/input.txt"
    main(file_path)
