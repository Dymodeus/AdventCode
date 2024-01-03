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


def count_arrangements(line: str, number: list, ind: int):
    total_sum = 0
    q_indices = [m.start() for m in re.finditer("\?", line)]
    for combo in itertools.combinations(q_indices, number_of_hashtags_needed[ind]):
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
    q_indices = [m.start() for m in re.finditer("\?", line)]
    for combo in itertools.combinations(q_indices, places_to_fill):
        new_line = line
        for index in combo:
            new_line = new_line[:index] + "#" + new_line[index + 1:]
        new_line = new_line.replace("?", ".")
        if check_correct(new_line, number):
            total_sum += 1
            if new_line[0] == "#" and new_line[-1] == ".":
                left_sum += 1
            if new_line[-1] == "#" and new_line[0] == ".":
                right_sum += 1
            if new_line[0] == "#" and new_line[-1] == "##":
                both_sum += 1
    print(left_sum, right_sum, both_sum)
    return total_sum ** 5 - (4 * right_sum * left_sum) ** 4 - (5 * both_sum) ** 10


def task1():
    sums = 0
    ind = 0
    for line, number in zip(lines, numbers):
        sums += count_arrangements(line, number, ind)
        ind += 1
    print(f"The answer to task 1 is {sums}\n")


def task2():
    sums = 0
    # for ind, (line, number) in enumerate(zip(lines, numbers)):
    #     if ind == 0:
    #         print(line, number)
    #     total_sum, left_sum, right_sum = count_arrangements(line, number, ind)
    #     sums += total_sum
    print(count_arrangements_2("?###?????????", [3, 2, 1], 3))

    print(f"The answer to task 2 is {sums}\n")


if __name__ == "__main__":
    # task1()
    task2()
