
from typing import List

from src.day04.models.ScratchCard import ScratchCard
from src.day04.models.ScratchCardLine import ScratchCardLine


def read_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def get_n_scorecards(lines):
    scratch_cards: List[ScratchCard] = [ScratchCardLine(line).to_scratch_card() for line in lines]
    matched_numbers = [scratch_card.get_matched_numbers() for scratch_card in scratch_cards]
    number_of_each_card = [1 for _ in matched_numbers]

    for scored_index in range(len(number_of_each_card)):
        n_scratchcards_ahead_won = score_scratchcard(matched_numbers[scored_index])
        n_scratchcards_won = number_of_each_card[scored_index]
        for award_index in range(
                scored_index+1,
                min(scored_index + 1 + n_scratchcards_ahead_won, len(number_of_each_card))
        ):
            number_of_each_card[award_index] += n_scratchcards_won

    return sum(number_of_each_card)


def score_scratchcard(matched_numbers):
    return len(matched_numbers)



def main(file_path):
    n_scorecards = get_n_scorecards(
        read_lines(file_path)
    )

    print(f"you won {n_scorecards} scorecards")
    return n_scorecards


if __name__ == "__main__":
    file_path = "input/input.txt"
    main(file_path)
