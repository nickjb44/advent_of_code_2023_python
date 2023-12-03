
class CubeRound:

    def __init__(self, cubes):
        self.color_to_cube = {}
        for cube in cubes:
            self.color_to_cube[cube.color] = cube
