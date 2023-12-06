from config import input_path
import re
import os

with open(os.path.join(input_path, "input3.txt"), "r") as file:
    lines = file.readlines()


def check_for_chars(x1, x2, y1, y2):
    flag = False
    for x in range(x1, x2):
        for y in range(y1, y2):
            if (not lines[y][x].isalnum()) and (lines[y][x] != "."):
                flag = True
    return flag


def make_numbers_list():
    numbers = []

    for ind, line in enumerate(lines):
        numbers.append([(int(m[0]), max(m.span()[0] - 1, 0), min(m.span()[1] + 1, len(line) - 1)) for m
                        in re.finditer(r"\d+", line)])
    return numbers


def task1():
    sum_of_numbers = 0
    numbers = make_numbers_list()
    # check rows
    for ind, line in enumerate(numbers):
        # check the numbers in the line
        for number in line:
            line1 = max(ind - 1, 0)
            line2 = min(ind + 2, 140)
            if check_for_chars(number[1], number[2], line1, line2):
                sum_of_numbers += number[0]
    print(f"The answer for task 1 is {sum_of_numbers}\n")


def task2():
    gears = []

    for ind, line in enumerate(lines):
        gears.append([(max(m.span()[0] - 1, 0), min(m.span()[1] + 1, len(line) - 1)) for m
                      in re.finditer(r"[*]", line)])

    numbers = make_numbers_list()


    print(gears)


if __name__ == "__main__":
    task1()


