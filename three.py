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


def check_gear_neighbors(coords, numbers):
    row, column = coords[0], coords[1]
    list_of_neighbors = []
    for line_ind in range(max(row - 1, 0), min(row + 2, 140)):
        for number in numbers[line_ind]:
            if column in range(number[1], number[2]):
                # print(f"Gear on coords: {coords}, number {number[0]} on line: {line_ind}")
                list_of_neighbors.append(number[0])
    if len(list_of_neighbors) == 2:
        # print(f"it works for: {list_of_neighbors}")
        return list_of_neighbors[0] * list_of_neighbors[1]
    else:
        return 0


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
    # print(f"The answer for task 1 is {sum_of_numbers}\n")
    return sum_of_numbers


def task2():
    gears = []

    for ind, line in enumerate(lines):
        gears.append([(max(m.span()[0] - 1, 0), min(m.span()[1] + 1, len(line) - 1)) for m
                      in re.finditer(r"[*]", line)])

    numbers = make_numbers_list()

    sum_of_powers = 0

    for ind, line in enumerate(gears):
        for gear in line:
            sum_of_powers += check_gear_neighbors((ind, gear[0] + 1), numbers)

    return sum_of_powers


if __name__ == "__main__":
    print(f"The answer to task 1 is:\n {task1()}\n")
    print(f"The answer to task 2 is:\n {task2()}")


