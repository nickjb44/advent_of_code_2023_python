from src.day06.models.Race import Race


def main(file_path):
    with open(file_path) as race_file:
        for line in race_file:
            if "Time" in line:
                times = line.rstrip().split(":")[1].split()
            elif "Distance" in line:
                distances = line.rstrip().split(':')[1].split()
    races = [Race(time=int(time), record_distance=int(distance)) for time, distance in zip(times, distances)]

    ways_to_win_by_race = [len(race.brute_force_check_ways_to_win()) for race in races]

    answer = 1
    for ways_to_win in ways_to_win_by_race:
        answer *= ways_to_win
    return answer



if __name__ == "__main__":
    file_path = "input/input.txt"
    margin_of_error = main(file_path)

    print(f"the margin of error is: {margin_of_error}")
