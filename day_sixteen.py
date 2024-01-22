from config import input_path
import os
import numpy as np

test = False

if test:
    lines = np.array([list(line.rstrip()) for line in open(os.path.join(input_path, "test_input16.txt"), "r+")])
else:
    lines = np.array([list(line.rstrip()) for line in open(os.path.join(input_path, "input16.txt"), "r+")])
# print(test_line)

# print([[None]*len(test_line[0])]*len(test_line))

direction_changes = {"N": [-1, 0], "E": [0, 1], "S": [1, 0], "W": [0, -1]}
new_direction_back = {"N": "W", "E": "S", "S": "E", "W": "N"}
new_direction_forward = {"N": "E", "E": "N", "S": "W", "W": "S"}


def get_energized_tiles(start_tile, start_direction):
    directions = np.empty_like(lines)
    energized = np.empty_like(lines)
    beams = [[start_tile[0], start_tile[1], start_direction]]  # row, column, direction
    # directions[start_tile[0]][start_tile[1]] = start_direction
    # energized[start_tile[0]][start_tile[1]] = "#"
    step = 0
    while True:
        step += 1
        new_beams = beams.copy()
        to_delete = []
        for ind, beam in enumerate(beams):
            new_row = beam[0] + direction_changes[beam[2]][0]
            new_column = beam[1] + direction_changes[beam[2]][1]
            if new_row < 0 or new_column < 0 or new_row >= len(lines) or new_column >= len(lines[0]):
                # new_beams.pop(ind)
                to_delete.append(ind)
            else:
                new_beams[ind][0], new_beams[ind][1] = new_row, new_column
                energized[new_row, new_column] = "#"
                # print(beams)
                if lines[new_row][new_column] == "\\":
                    new_direction = new_direction_back[beam[2]]
                    new_beams[ind][2] = new_direction
                    if new_direction in directions[new_row, new_column]:
                        # new_beams.pop(ind)
                        to_delete.append(ind)
                    else:
                        directions[new_row, new_column] += new_direction
                elif lines[new_row][new_column] == "/":
                    new_direction = new_direction_forward[beam[2]]
                    new_beams[ind][2] = new_direction
                    if new_direction in directions[new_row, new_column]:
                        # new_beams.pop(ind)
                        to_delete.append(ind)
                    else:
                        directions[new_row, new_column] += new_direction
                elif lines[new_row][new_column] == "|" and (beam[2] == "E" or beam[2] == "W"):
                    if "S" in directions[new_row, new_column]:
                        # new_beams.pop(ind)
                        to_delete.append(ind)
                    else:
                        new_beams[ind][2] = "S"
                        directions[new_row, new_column] += "S"
                    if "N" not in directions[new_row, new_column]:
                        new_beams.append([new_row, new_column, "N"])
                        directions[new_row, new_column] += "N"
                elif lines[new_row][new_column] == "-" and (beam[2] == "N" or beam[2] == "S"):
                    if "E" in directions[new_row, new_column]:
                        # new_beams.pop(ind)
                        to_delete.append(ind)
                    else:
                        new_beams[ind][2] = "E"
                        directions[new_row, new_column] += "E"
                    if "W" not in directions[new_row, new_column]:
                        new_beams.append([new_row, new_column, "W"])
                        directions[new_row, new_column] += "W"
                else:
                    if beam[2] in directions[new_row, new_column]:
                        to_delete.append(ind)
                    else:
                        directions[new_row, new_column] += beam[2]
        for ind in to_delete[::-1]:
            new_beams.pop(ind)
        beams = new_beams.copy()
        # if step % 100 == 0:
        #     print(to_delete)
        #     print(beams)
        if len(beams) == 0:
            break

    return np.sum(energized == "#")


def task1():
    answer = get_energized_tiles([2, -1], "E")
    print(f"The answer to part one is {answer}\n")


def task2():
    array_energized = []
    for column in [-1, len(lines[0])]:
        for row in range(len(lines)):
            start_line = [row, column]
            start_direction = "E" if column == -1 else "W"
            sum_of_energized = get_energized_tiles(start_line, start_direction)
            array_energized.append(sum_of_energized)
            if row % 10 == 0:
                print(f"Row {row} done.\n")
    for row in [-1, len(lines)]:
        for column in range(len(lines[0])):
            start_line = [row, column]
            start_direction = "S" if row == -1 else "N"
            sum_of_energized = get_energized_tiles(start_line, start_direction)
            array_energized.append(sum_of_energized)
            if column % 10 == 0:
                print(f"Column {column} done.\n")
    print(array_energized)
    print(f"The answer to part two is {max(array_energized)}")  # 8167 is too low


if __name__ == "__main__":
    # task1()
    task2()
