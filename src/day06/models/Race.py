class Race:
    def __init__(self, time, record_distance):
        self.time = time
        self.record_distance = record_distance

    def brute_force_check_ways_to_win(self):
        ways_to_win = set()
        for time_winding in range(0, self.time + 1):
            distance_travelled = self.simulate_race(time_winding)
            if distance_travelled > self.record_distance:
                ways_to_win.add(time_winding)
        return ways_to_win

    def simulate_race(self, time_winding):
        remaining_time = self.time - time_winding
        return time_winding * remaining_time
