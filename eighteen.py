from config import input_path
import os
import numpy as np

test = True
if test:
    lines = [line.rstrip().split() for line in open(os.path.join(input_path, "test_input18.txt"))]
else:
    lines = [line.rstrip().split() for line in open(os.path.join(input_path, "input18.txt"))]
print(lines)
directions = {"R": np.array([0, 1]), "L": np.array([0, -1]), "D": np.array([1, 0]), "U": np.array([-1, 0])}

current_row, current_col = 0, 0
coords = np.empty((len(lines) + 1, 2), dtype=int)
coords[0, :] = np.array([0, 0])

for ind, line in enumerate(lines):
    direction, meters = line[0], int(line[1])
    coords[ind + 1, :] = coords[ind, :] + meters * directions[direction]

coords = coords - np.tile(np.min(coords, 0), (np.shape(coords)[0], 1))
dig_plan = np.full(np.max(coords, 0) + np.array([1, 1]), fill_value=".")
row, col = coords[0, 0], coords[0, 1]
dig_plan[row, col] = "#"
# print(coords)

for ind, line in enumerate(lines):
    direction, meters = line[0], int(line[1])
    match direction:
        case "R":
            for i in range(1, meters + 1):
                dig_plan[row, col + i] = "#"
        case "L":
            for i in range(1, meters + 1):
                dig_plan[row, col - i] = "#"
        case "U":
            for i in range(1, meters + 1):
                dig_plan[row - i, col] = "#"
        case "D":
            for i in range(1, meters + 1):
                dig_plan[row + i, col] = "#"
    row, col = coords[ind + 1, 0], coords[ind + 1, 1]
print(dig_plan)
