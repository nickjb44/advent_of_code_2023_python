class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return (
                isinstance(other, Coordinate) and
                self.row == other.row and
                self.col == other.col
        )

    def __hash__(self):
        '''
        doing this so I can check if one is in the set
        '''
        return hash((self.row, self.col))
