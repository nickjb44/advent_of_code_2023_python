from src.day09.models.OASIS import OASIS


def main(file_path):
    with open(file_path) as sequences_file:
        OASIS_list = []
        for line in sequences_file:
            line = line.rstrip()
            nums = [int(string_num) for string_num in line.split()]
            OASIS_list.append(OASIS(nums))

    sum_of_extrapolated = 0
    for oasis in OASIS_list:
        extrapolated_value = oasis.calculate_next_in_sequence()
        sum_of_extrapolated += extrapolated_value
    return sum_of_extrapolated



if __name__ == "__main__":
    file_path = "input/input.txt"
    extrapolated_sum = main(file_path)
    print(f'sum_of_extrapolated is {extrapolated_sum}')
