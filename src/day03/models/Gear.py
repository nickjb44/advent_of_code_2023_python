class Gear:
    def __init__(self, neighbor_one, neighbor_two):
        self.neighbor_one = neighbor_one
        self.neighbor_two = neighbor_two

    def calculate_gear_ratio(self):
        return self.neighbor_one * self.neighbor_two
