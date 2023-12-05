from typing import List

from src.day04.models.ScratchCard import ScratchCard
from src.day04.models.ScratchCardLine import ScratchCardLine


def read_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def calculate_total_winnings(lines):
    scratch_cards: List[ScratchCard] = [ScratchCardLine(line).to_scratch_card() for line in lines]
    matched_numbers = [scratch_card.get_matched_numbers() for scratch_card in scratch_cards]

    return sum(
        map(
            score_scratchcard,
            matched_numbers
        )
    )


def score_scratchcard(matched_numbers):
    if not matched_numbers:
        return 0
    return 2 ** (len(matched_numbers)-1)



def main(file_path):
    total_winnings = calculate_total_winnings(
        read_lines(file_path)
    )

    print(f"your total winnings are {total_winnings}")
    return total_winnings


if __name__ == "__main__":
    file_path = "input/input.txt"
    main(file_path)
