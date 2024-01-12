from config import input_path
import os
import numpy as np

lines = np.array([list(line.rstrip()) for line in open(os.path.join(input_path, "input16.txt"), "r+")])
directions = np.empty_like(lines)
energized = np.empty_like(lines)
# print([line[-1] == "\\" for line in lines])

test_line = np.array([list(line.rstrip()) for line in open(os.path.join(input_path, "test_input16.txt"), "r+")])
test_directions = np.empty_like(test_line)
test_energized = np.empty_like(test_line)
# print(test_line)

# print([[None]*len(test_line[0])]*len(test_line))

direction_changes = {"N": [-1, 0], "E": [0, 1], "S": [1, 0], "W": [0, -1]}
new_direction_back = {"N": "W", "E": "S", "S": "E", "W": "N"}
new_direction_forward = {"N": "E", "E": "N", "S": "W", "W": "S"}


test_energized[0][0] = "#"
test_directions[0][0] = "E"
# print(test_directions)


def get_energized_tiles(start_tile, start_direction):
    beams = [[start_tile[0], start_tile[1], start_direction]]  # row, column, direction
    directions[start_tile[0]][start_tile[1]] = start_direction
    energized[start_tile[0]][start_tile[1]] = "#"
    while True:
        for ind, beam in enumerate(beams):
            new_row = beam[0] + direction_changes[beam[2]][0]
            new_column = beam[1] + direction_changes[beam[2]][1]
            if new_row < 0 or new_column < 0 or new_row >= len(lines) or new_column >= len(lines[0]):
                beams.pop(ind)
                break
            beams[ind][0], beams[ind][1] = new_row, new_column
            energized[new_row, new_column] = "#"
            # print(beams)
            if lines[new_row][new_column] == "\\":
                new_direction = new_direction_back[beam[2]]
                beams[ind][2] = new_direction
                if new_direction in directions[new_row, new_column]:
                    beams.pop(ind)
                else:
                    directions[new_row, new_column] += new_direction
            elif lines[new_row][new_column] == "/":
                new_direction = new_direction_forward[beam[2]]
                beams[ind][2] = new_direction
                if new_direction in directions[new_row, new_column]:
                    beams.pop(ind)
                else:
                    directions[new_row, new_column] += new_direction
            elif lines[new_row][new_column] == "|" and (beam[2] == "E" or beam[2] == "W"):
                if "S" in directions[new_row, new_column]:
                    beams.pop(ind)
                else:
                    beams[ind][2] = "S"
                    directions[new_row, new_column] += "S"
                if "N" not in directions[new_row, new_column]:
                    beams.append([new_row, new_column, "N"])
                    directions[new_row, new_column] += "N"
            elif lines[new_row][new_column] == "-" and (beam[2] == "N" or beam[2] == "S"):
                if "E" in directions[new_row, new_column]:
                    beams.pop(ind)
                else:
                    beams[ind][2] = "E"
                    directions[new_row, new_column] += "E"
                if "W" not in directions[new_row, new_column]:
                    beams.append([new_row, new_column, "W"])
                    directions[new_row, new_column] += "W"
            else:
                directions[new_row, new_column] += beam[2]

        if len(beams) == 0:
            break

    return np.sum(energized == "#")


def task1():
    answer = get_energized_tiles([0, 0], "S")
    print(f"The answer to part one is {answer}\n")


def task2():
    max_energized = 0

    print("")


if __name__ == "__main__":
    task1()
