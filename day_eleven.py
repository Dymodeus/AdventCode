import numpy as np
from itertools import combinations

from config import input_path
import os

lines = [list(line.rstrip()) for line in open(os.path.join(input_path, "input11.txt"))]
# print(lines)
# lines = ["...#......", ".......#..", "#.........", "..........", "......#...", ".#........", ".........#",
#          "..........", ".......#..", "#...#....."]
# lines = [list(line) for line in lines]

empty_ind_row = []
empty_ind_col = []
for ind, line in enumerate(lines):
    if "#" not in line:
        empty_ind_row.append(ind)

lines_t = np.array(lines).T
for ind, line in enumerate(lines_t):
    if "#" not in line:
        empty_ind_col.append(ind)
# print(empty_ind_row, empty_ind_col)


def calc_distance(pos1, pos2, n):
    dist = sum(np.abs(np.array(pos2) - np.array(pos1)))
    for i in empty_ind_row:
        if i in range(min(pos1[0], pos2[0]), max(pos1[0], pos2[0])):
            dist += (n - 1)
    for i in empty_ind_col:
        if i in range(min(pos1[1], pos2[1]), max(pos1[1], pos2[1])):
            dist += (n - 1)
    return dist


def get_galaxy_indices():
    coords = []
    for x in range(len(lines)):
        for y in range(len(lines_t)):
            if lines[x][y] == "#":
                coords.append((x,y))
    return coords


def task1():
    coords = get_galaxy_indices()
    sum_of_len = 0
    for star1, star2 in combinations(coords, 2):
        dist = calc_distance(star1, star2, 2)
        # print((star1, star2), dist)
        sum_of_len += dist
    # print(i)
    print(sum_of_len)


def task2():
    coords = get_galaxy_indices()
    sum_of_len = []
    for star1, star2 in combinations(coords, 2):
        dist = calc_distance(star1, star2, 1000000)
        # print(dist)
        sum_of_len.append(dist)
    # print(i)
    print(sum_of_len)


if __name__ == "__main__":
    task1()
    task2()
