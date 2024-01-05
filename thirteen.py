from config import input_path
import os
import numpy as np

lines = [line.rstrip() for line in open(os.path.join(input_path, "input13.txt"))]

empty_lines = []
for ind, line in enumerate(lines):
    if not line:
        empty_lines.append(ind)

mirrors = [lines[:empty_lines[0]]]

for ind1, ind2 in zip(empty_lines[:-1], empty_lines[1:]):
    mirrors.append(lines[ind1+1:ind2])

mirrors.append(lines[empty_lines[-1] + 1:])


def check_hor_reflections(mirror: list):
    rows = len(mirror)
    for row in range(rows - 1):
        if row + 1 < rows / 2:
            if mirror[:row + 1][::-1] == mirror[row + 1:2 * row + 2]:
                return row + 1
        if row + 1 >= rows / 2:
            if mirror[row + 1:][::-1] == mirror[2 * (row + 1) - rows:row + 1]:
                return row + 1


def check_smudged_hor_reflection(mirror: list):
    rows = len(mirror)
    for row in range(rows - 1):
        if row + 1 < rows / 2:
            x = np.reshape(np.array([list(a) for a in mirror[row + 1:2 * row + 2]]), -1)
            y = np.reshape(np.array([list(a) for a in mirror[:row + 1]][::-1]), -1)
            if len([a for a in zip(x, y) if a[0] != a[1]]) == 1:
                return row + 1
        if row + 1 >= rows / 2:
            x = np.reshape(np.array([list(a) for a in mirror[2 * (row + 1) - rows:row + 1]]), -1)
            y = np.reshape(np.array([list(a) for a in mirror[row + 1:]][::-1]), -1)
            if len([a for a in zip(x, y) if a[0] != a[1]]) == 1:
                return row + 1


def check_vert_reflections(mirror: list, smudge=False):
    # cols = len(list(mirror[0]))
    mirror_t = np.array([list(x) for x in mirror]).T
    mirror_t = ["".join(x) for x in mirror_t]
    # print(mirror_t)
    if smudge:
        col = check_smudged_hor_reflection(mirror_t)
    else:
        col = check_hor_reflections(mirror_t)
    return col


test_vert = ["#.##..##.", "..#.##.#.", "##......#", "##......#", "..#.##.#.", "..##..##.", "#.#.##.#."]
test_hor = ["#...##..#", "#....#..#", "..##..###", "#####.##.", "#####.##.", "..##..###", "#....#..#"]


def task1():
    total_sum = 0
    arr = []
    for mirror in mirrors:

        row, col = check_hor_reflections(mirror), check_vert_reflections(mirror, smudge=False)

        if row:
            arr.append(f"r{row}")
            total_sum += 100 * row
        if col:
            arr.append(f"c{col}")
            total_sum += col
    print(f"The answer to part one is {total_sum}\n")


def task2():
    total_sum = 0
    arr = []
    for mirror in mirrors:

        row, col = check_smudged_hor_reflection(mirror), check_vert_reflections(mirror, smudge=True)

        if row:
            arr.append(f"r{row}")
            total_sum += 100 * row
        if col:
            arr.append(f"c{col}")
            total_sum += col
    print(f"The answer to part two is {total_sum}\n")


if __name__ == "__main__":
    # task1()
    task2()
