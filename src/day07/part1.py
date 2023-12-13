from src.day07.models.Hand import Hand


def main(file_path):
    with open(file_path) as hands_file:
        hands = []
        for line in hands_file:
            line = line.rstrip()
            (card_string, bid) = line.split()
            hands.append(Hand(card_string, bid))
    hands.sort()

    total_winnings = 0
    for hand_index in range(len(hands)):
        hand = hands[hand_index]
        rank = hand_index + 1

        total_winnings += rank * hand.bid

    return total_winnings


if __name__ == "__main__":
    file_path = "input/input.txt"
    total_winnings = main(file_path)

    print(f'your total winnings were {total_winnings}')

