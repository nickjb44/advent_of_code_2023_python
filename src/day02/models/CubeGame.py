from src.day02.models.Cube import Color, Cube
from src.day02.models.CubeBag import CubeBag


class CubeGame:
    def __init__(self, rounds, cube_bag=None, game_id=None):
        self.rounds = rounds
        self.cube_bag = cube_bag
        self.game_id = game_id

    def get_max_seen_of_color(self, color):
        max_seen = 0

        for round in self.rounds:
            if color in round.color_to_cube:
                max_seen = max(max_seen, round.color_to_cube[color].count)

        return max_seen

    def is_valid(self):
        return not any(
            self.get_max_seen_of_color(color) > self.cube_bag.color_to_cube[color].count
            for color in Color
        )

    def get_fewest_cubes_to_be_valid(self):
        min_red = self.get_max_seen_of_color(Color.RED)
        min_green = self.get_max_seen_of_color(Color.GREEN)
        min_blue = self.get_max_seen_of_color(Color.BLUE)

        return CubeBag([
            Cube(Color.RED, min_red),
            Cube(Color.GREEN, min_green),
            Cube(Color.BLUE, min_blue),
        ])

    def set_cube_bag(self, cube_bag):
        # there's probably a cleaner way to do this
        self.cube_bag = cube_bag
        return self
