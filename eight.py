from config import input_path
import os

with open(os.path.join(input_path, "input8.txt"), "r") as file:
    lines = [line.strip() for line in file.readlines()]

instructions = lines[0]
num_of_instructions = len(instructions)
maps = dict([(x.split(" = ")[0], (x.split(" = ")[1].split(", ")[0].lstrip("("),
                                  x.split(" = ")[1].split(", ")[1].rstrip(")"))) for x in lines[2:]])
step_map = {"L": 0, "R": 1}


def task1():
    location = "AAA"
    steps = 0
    while location != "ZZZ":
        instruction = instructions[steps % num_of_instructions]
        location = maps[location][step_map[instruction]]
        steps += 1
    print(steps)


if __name__ == "__main__":
    task1()
