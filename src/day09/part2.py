from src.day09.models.OASIS import OASIS


def main(file_path):
    with open(file_path) as sequences_file:
        OASIS_list = []
        for line in sequences_file:
            line = line.rstrip()
            nums = [int(string_num) for string_num in line.split()]
            OASIS_list.append(OASIS(nums))

    sum_of_pretrapolated = 0
    for oasis in OASIS_list:
        pretrapolated_value = oasis.alternate_calculate_previous_in_sequence()
        sum_of_pretrapolated += pretrapolated_value
    return sum_of_pretrapolated



if __name__ == "__main__":
    file_path = "input/input.txt"
    pretrapolated_sum = main(file_path)
    print(f'sum_of_pretrapolated is {pretrapolated_sum}')
