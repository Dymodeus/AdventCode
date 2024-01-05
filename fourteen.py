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


def slide_rocks(array: np.array):
    o_locations = np.argwhere(array == "O")
    for location in o_locations:
        row, col = location
        while True:
            if row == 0:
                break
            if array[row - 1, col] != ".":
                break
            row -= 1
        # print(f"Changing from {location} to {[row, col]}\n")
        array[location[0], location[1]] = "."
        array[row, col] = "O"
    return array


def task1():
    slided_array = slide_rocks(lines_np)
    total_sum = 0
    for row, line in enumerate(slided_array):
        for col in line:
            if col == "O":
                total_sum += num_of_rows - row

    print(f"The answer to part one is {total_sum}\n")


if __name__ == "__main__":
    task1()
