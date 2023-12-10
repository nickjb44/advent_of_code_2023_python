class Seed:
    def __init__(self, seed_id):
        self.seed_id = seed_id
        # ideally this would map to resource of type seed but my head is pretzeling here
        self.category = "seed"

    def seed_to_location(self, almanac):
        # need to do that recursive mapping after finding a path here
        # might be better to do it at almanac level, idk
        pass


