from config import input_path
import os
import numpy as np
import matplotlib.pyplot as plt

test = False
if test:
    lines = [line.rstrip().split() for line in open(os.path.join(input_path, "test_input18.txt"))]
else:
    lines = [line.rstrip().split() for line in open(os.path.join(input_path, "input18.txt"))]
# print(lines)
directions = {"R": np.array([0, 1]), "L": np.array([0, -1]), "D": np.array([1, 0]), "U": np.array([-1, 0])}


def create_grid():
    current_row, current_col = 0, 0
    coords = np.empty((len(lines) + 1, 2), dtype=int)
    coords[0, :] = np.array([0, 0])

    for ind, line in enumerate(lines):
        direction, meters = line[0], int(line[1])
        coords[ind + 1, :] = coords[ind, :] + meters * directions[direction]

    coords = coords - np.tile(np.min(coords, 0), (np.shape(coords)[0], 1))
    dig_plan = np.full(np.max(coords, 0) + np.array([1, 1]), dtype=bool, fill_value=False)
    row, col = coords[0, 0], coords[0, 1]
    dig_plan[row, col] = True
    # print(coords)

    for ind, line in enumerate(lines):
        direction, meters = line[0], int(line[1])
        match direction:
            case "R":
                for i in range(1, meters + 1):
                    dig_plan[row, col + i] = True
            case "L":
                for i in range(1, meters + 1):
                    dig_plan[row, col - i] = True
            case "U":
                for i in range(1, meters + 1):
                    dig_plan[row - i, col] = True
            case "D":
                for i in range(1, meters + 1):
                    dig_plan[row + i, col] = True
        row, col = coords[ind + 1, 0], coords[ind + 1, 1]
    return dig_plan
# print(dig_plan)
# print(np.transpose(dig_plan[1:-1, :]))


def task1():
    dig_plan = create_grid()
    print(dig_plan)
    plt.figure()
    plt.imshow(dig_plan, cmap=plt.cm.gray)
    dig_plan_one = dig_plan.copy()

    for row, line in enumerate(dig_plan[1:-1][:], 1):
        inner = False
        edge = False
        dir_edge = [0, 1]
        for col, cube in enumerate(line):
            if cube and inner and not edge:
                inner = False
                edge = True
                if dig_plan[row - 1, col]:
                    dir_edge[0] = "up"
                else:
                    dir_edge[0] = "down"
            elif cube and not inner and not edge:
                inner = True
                edge = True
                if dig_plan[row - 1, col]:
                    dir_edge[0] = "up"
                else:
                    dir_edge[0] = "down"
            elif cube and edge:
                if dig_plan[row - 1, col]:
                    dir_edge[1] = "up"
                else:
                    dir_edge[1] = "down"
            elif not cube and inner:
                if dir_edge[0] == dir_edge[1]:
                    inner = not inner
                else:
                    dig_plan_one[row, col] = True
                edge = False
                dir_edge = [0, 1]
            elif not cube and not inner:
                if dir_edge[0] == dir_edge[1]:
                    inner = not inner
                    dig_plan_one[row, col] = True
                edge = False
                dir_edge = [0, 1]

    # print(dig_plan)
    print(f"The answer to part one is {np.count_nonzero(dig_plan_one)}\n")    # 16257 too low
    # dig_plan_total = dig_plan_one and dig_plan_two

    plt.figure()
    plt.imshow(dig_plan_one, cmap=plt.cm.gray)

    plt.show()


if __name__ == "__main__":
    task1()
