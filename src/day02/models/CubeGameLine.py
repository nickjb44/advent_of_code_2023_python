import re

from src.day02.models.CubeGame import CubeGame
from src.utils.models.Line import Line

from src.day02.models.Cube import Color, Cube
from src.day02.models.CubeRound import CubeRound


def chunk_to_n_of_color(color, chunk):
    pattern = rf'(\d+) {color}'
    match = re.search(pattern, chunk)

    if not match:
        return '0'

    return match.group(1)


class CubeGameLine(Line):

    def to_game(self):
        '''
        transforms the line into a game type
        with an id parameter and list of rounds
        :return:
        '''
        return CubeGame(
            rounds=self.to_round_list(),
            game_id=int(self.get_game_id())
        )

    def to_round_list(self):
        '''
        transforms the line into a list of rounds
        where each round contains color-count pairs
        :return:
        '''
        chunks = self.get_chunks()
        return [self.chunk_to_round(chunk) for chunk in chunks]

    def get_chunks(self):
        return self.content.split(':')[1].split(';')

    def get_game_id(self):
        pattern = r'Game (\d+):'
        match = re.search(pattern, self.content)

        if not match:
            raise ValueError("No game id found, Panic!")

        return match.group(1)

    @staticmethod
    def chunk_to_round(chunk):
        # this is ugly and I shouldn't be doing all that in this method
        # but I wrote it already and don't want to refactor...

        n_red = int(chunk_to_n_of_color(Color.RED.name.lower(), chunk))
        n_green = int(chunk_to_n_of_color(Color.GREEN.name.lower(), chunk))
        n_blue = int(chunk_to_n_of_color(Color.BLUE.name.lower(), chunk))

        return CubeRound([
            Cube(Color.RED, n_red),
            Cube(Color.GREEN, n_green),
            Cube(Color.BLUE, n_blue)
        ]
        )
