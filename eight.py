from config import input_path
import time
import math
import os

start_time = time.time()

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
    print(f"The answer to part one is {steps}\n")


def task2():
    locations = [x for x in maps.keys() if x.endswith("A")]
    steps = []
    for location in locations:
        steps.append(0)
        while not location.endswith("Z"):
            instruction = instructions[steps[-1] % num_of_instructions]
            location = maps[location][step_map[instruction]]
            steps[-1] += 1

    print(f"The answer to part two is {math.lcm(*steps)}\n")


if __name__ == "__main__":
    task1()
    task2()
    print(f"Total runtime: {time.time() - start_time} seconds.")
