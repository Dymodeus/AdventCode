import re

import numpy as np

from config import input_path
import os

lines = [line.rstrip() for line in open(os.path.join(input_path, "input14.txt"))]
num_of_rows = len(lines)
x = [list(line) for line in lines]
lines_np = np.array(x, dtype=str)


test_pattern = ["O....#....", "O.OO#....#", ".....##...", "OO.#O....O", ".O.....O#.", "O.#..O.#.#", "..O..#O..O",
                ".......O..", "#....###..", "#OO..#...."]

test_array = np.array([list(x) for x in test_pattern])


def slide_rocks(array: np.array, direction: str):
    # print(direction)
    match direction:
        case "n":
            o_locations = np.argwhere(array == "O")
        case "w":
            o_locations = np.argwhere(array == "O")
        case "s":
            o_locations = np.argwhere(array == "O")[::-1]
        case "e":
            o_locations = np.argwhere(array == "O")[::-1]
        case _:
            o_locations = np.argwhere(array == "O")

    for location in o_locations:
        row, col = location
        while True:
            match direction:
                case "n":
                    if row == 0:
                        break
                    if array[row - 1, col] != ".":
                        break
                    row -= 1
                case "w":
                    if col == 0:
                        break
                    if array[row, col - 1] != ".":
                        break
                    col -= 1
                case "s":
                    if row == np.shape(array)[0] - 1:
                        break
                    if array[row + 1, col] != ".":
                        break
                    row += 1
                case "e":
                    if col == np.shape(array)[1] - 1:
                        break
                    if array[row, col + 1] != ".":
                        break
                    col += 1
        # print(f"Changing from {location} to {[row, col]}\n")
        array[location[0], location[1]] = "."
        array[row, col] = "O"
    return array


def calc_load(array):
    load = 0
    for row, line in enumerate(array):
        for col in line:
            if col == "O":
                load += num_of_rows - row
    return load


def task1():
    slided_array = slide_rocks(lines_np, "n")
    print(f"The answer to part one is {calc_load(slided_array)}\n")


def one_cycle(array):
    for direction in ["n", "w", "s", "e"]:
        array = slide_rocks(array, direction)
        # print(array)
    return array


def task2():
    array = test_array.copy()
    cycle = 0
    while True:
        array = one_cycle(array)
        cycle += 1
        # print(array)
        # print(test_array)
        if cycle % 1000 == 0:
            print(cycle)
        if np.array_equal(array, test_array):
            break
    print(cycle)


if __name__ == "__main__":
    # task1()
    task2()
