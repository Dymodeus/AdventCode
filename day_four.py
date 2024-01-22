from config import input_path
import numpy as np
import os


def parse_input():
    with open(os.path.join(input_path, "input4.txt")) as file:
        lines = file.readlines()
    table_of_winners = [line.split(":")[1].split("|")[0].split() for line in lines]
    table_of_entries = [line.split(":")[1].split("|")[1].split() for line in lines]
    return table_of_winners, table_of_entries


def task1():
    table_of_winners, table_of_entries = parse_input()
    sum_of_points = sum([(lambda ind: np.floor(2 ** (len([int(x) for x in table_of_entries[ind] if x in
                                                          table_of_winners[ind]]) - 1)))(ind)
                         for ind, line in enumerate(table_of_entries)])
    print(f"The answer to part 1 is {sum_of_points}\n\n")


def task2():
    table_of_winners, table_of_entries = parse_input()
    amount_of_cards = np.ones(len(table_of_entries))
    for ind, line in enumerate(table_of_entries):
        matching_numbers = len([x for x in line if x in table_of_winners[ind]])
        for i in range(matching_numbers):
            amount_of_cards[ind + i + 1] += amount_of_cards[ind]
    print(f"The answer to part 2 is {sum(amount_of_cards)}")


if __name__ == "__main__":
    task1()
    task2()
