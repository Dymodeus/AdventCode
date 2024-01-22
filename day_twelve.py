import re

from config import input_path
import os
import numpy as np
import itertools

lines = [line.rstrip().split()[0] for line in open(os.path.join(input_path, "input12.txt"))]
numbers = [line.rstrip().split()[1].split(",") for line in open(os.path.join(input_path, "input12.txt"))]
number_of_question = [line.count("?") for line in lines]
number_of_hashtags = [line.count("#") for line in lines]
numbers = [[int(x) for x in line] for line in numbers]
total_hashtags = [sum(x) for x in numbers]
number_of_hashtags_needed = [x - y for (x, y) in zip(total_hashtags, number_of_hashtags)]


def check_correct(row: str, number: list):
    return [len(x) for x in row.split(".") if x] == number


def count_arrangements(line: str, number: list, places_to_fill: int):
    total_sum = 0
    q_indices = [m.start() for m in re.finditer("\\?", line)]
    for combo in itertools.combinations(q_indices, places_to_fill):
        new_line = line
        for index in combo:
            new_line = new_line[:index] + "#" + new_line[index + 1:]
        new_line = new_line.replace("?", ".")
        if check_correct(new_line, number):
            total_sum += 1
    return total_sum


def count_arrangements_2(line: str, number: list, places_to_fill: int):
    total_sum = 0
    left_sum = 0
    right_sum = 0
    both_sum = 0
    q_indices = [m.start() for m in re.finditer("\\?", line)]

    for combo in itertools.combinations(q_indices, places_to_fill):
        new_line = line
        for index in combo:
            new_line = new_line[:index] + "#" + new_line[index + 1:]
        new_line = new_line.replace("?", ".")
        # print(new_line)
        if check_correct(new_line, number):
            total_sum += 1
            if new_line[0] == "#" and new_line[-1] == ".":
                left_sum += 1
            if new_line[-1] == "#" and new_line[0] == ".":
                right_sum += 1
            if new_line[0] == "#" and new_line[-1] == "#":
                both_sum += 1
    print(left_sum, right_sum, both_sum)
    # return total_sum ** 5 - (left_sum * right_sum) * (total_sum ** 4) - (both_sum * both_sum) ** 4
    return total_sum, left_sum, right_sum, both_sum


def task1():
    sums = 0
    ind = 0
    for line, number in zip(lines, numbers):
        sums += count_arrangements(line, number, number_of_hashtags_needed[ind])
        ind += 1
    print(f"The answer to task 1 is {sums}\n")


def task2():
    sums = 0
    for ind, (line, number) in enumerate(zip(lines, numbers)):
        if ind % 5 == 0:
            print(f"{ind} lines checked")
        total_sum_1 = count_arrangements(line, number, number_of_hashtags_needed[ind])
        total_sum_2 = count_arrangements(line + "?" + line, number * 2, 2 * number_of_hashtags_needed[ind])
        sums += total_sum_2 ** 4 // (total_sum_1 ** 3)
    # arrs = count_arrangements("????.######..#####.", [1, 6, 5], 1)
    # arrs1 = count_arrangements("????.######..#####.?????.######..#####.", [1, 6, 5, 1, 6, 5], 2)
    # print(arrs1 ** 4 // (arrs ** 3))

    print(f"The answer to task 2 is {sums}\n")


if __name__ == "__main__":
    # task1()
    task2()
