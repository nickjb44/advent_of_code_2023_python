from src.day06.models.Race import Race


def main(file_path):
    with open(file_path) as race_file:
        for line in race_file:
            if "Time" in line:
                times = line.rstrip().split(":")[1].split()
            elif "Distance" in line:
                distances = line.rstrip().split(':')[1].split()

    real_time = ""
    for time in times:
        real_time += time
    real_time = int(real_time)

    real_distance = ""
    for distance in distances:
        real_distance += distance
    real_distance = int(real_distance)

    race = Race(real_time, real_distance)

    return len(race.brute_force_check_ways_to_win())


if __name__ == "__main__":
    file_path = "input/input.txt"
    ways_to_win = main(file_path)

    print(f"the number of ways to win is: {ways_to_win}")
