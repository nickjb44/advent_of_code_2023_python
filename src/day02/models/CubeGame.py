from src.day02.models.Cube import Color


class CubeGame:
    def __init__(self, rounds, cube_bag=None, game_id=None):
        self.rounds = rounds
        self.cube_bag = cube_bag
        self.game_id = game_id

    def get_max_seen_of_color(self, color):
        max_seen = 0

        for round in self.rounds:
            if color not in round.color_to_cube:
                raise ValueError(f"color {color} not valid")
            max_seen = max(max_seen, round.color_to_cube[color].count)

        return max_seen

    def is_valid(self):
        return not any(
            self.get_max_seen_of_color(color) > self.cube_bag.color_to_cube[color].count
            for color in Color
        )

    def set_cube_bag(self, cube_bag):
        # there's probably a cleaner way to do this
        self.cube_bag = cube_bag
        return self

