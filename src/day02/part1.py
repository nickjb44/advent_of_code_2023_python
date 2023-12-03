from functools import reduce

from src.day01.models.CalibrationLine import CalibrationLine
from src.day02.models.Cube import Color, Cube
from src.day02.models.CubeBag import CubeBag
from src.day02.models.CubeGameLine import CubeGameLine


def read_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def calculate_calibration_total(lines):
    calibration_info_sums = map(
        lambda line: CalibrationLine(line).to_calibration_info().calculate_calibration_value(),
        lines
    )

    return reduce(
        lambda x, y: x + y,
        calibration_info_sums
    )


def calculate_sum_of_possible_games(lines, cube_bag):
    games = map(
        lambda line: CubeGameLine(line).to_game().set_cube_bag(cube_bag),
        lines
    )
    possible_games_ids = map(
        lambda possible_game: possible_game.game_id,
        filter(
            lambda game: game.is_valid(),
            games
        )
    )

    return reduce(
        lambda x, y: x + y,
        possible_games_ids
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
        read_lines(file_path),
        make_bag(n_red=12, n_green=13, n_blue=14)
    )

    print(f"the sum of possible game ids is {sum_of_possible_games}")
    return sum_of_possible_games


if __name__ == "__main__":
    file_path = "input/input.txt"
    main(file_path)
