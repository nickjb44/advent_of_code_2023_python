class CubeBag:

    def __init__(self, cubes):
        """
        same in type as CubeRound but semantically different
        A cube bag should be initialized once and used to track
        how many there are in the bag

        I don't like the duplication but I don't like using cubeRound either
        :param cubes:
        """
        self.color_to_cube = {}
        for cube in cubes:
            self.color_to_cube[cube.color] = cube
