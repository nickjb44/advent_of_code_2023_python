from functools import reduce

from src.day01.models.CalibrationLine import CalibrationLine
from src.day02.models.Cube import Color, Cube
from src.day02.models.CubeBag import CubeBag
from src.day02.models.CubeGameLine import CubeGameLine


def read_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def calculate_sum_of_possible_games(lines: CubeGameLine):
    games = map(
        lambda line: CubeGameLine(line).to_game(),
        lines
    )
    minimum_bags = map(
        lambda game: game.get_fewest_cubes_to_be_valid(),
        games
    )

    power_of_cubes = map(
        calculate_power_of_cubes,
        minimum_bags
    )

    return reduce(
        lambda x, y: x + y,
        power_of_cubes
    )

def calculate_power_of_cubes(minumum_bag: CubeBag):
    return (
            minumum_bag.color_to_cube[Color.RED].count *
            minumum_bag.color_to_cube[Color.GREEN].count *
            minumum_bag.color_to_cube[Color.BLUE].count
    )


def make_bag(n_red, n_green, n_blue):
    return CubeBag(
        [
            Cube(Color.RED, n_red),
            Cube(Color.GREEN, n_green),
            Cube(Color.BLUE, n_blue)
        ]
    )


def main(file_path):
    sum_of_possible_games = calculate_sum_of_possible_games(
        read_lines(file_path)
    )

    print(f"the sum of possible game ids is {sum_of_possible_games}")
    return sum_of_possible_games


if __name__ == "__main__":
    file_path = "input/input.txt"
    main(file_path)
