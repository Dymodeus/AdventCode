from config import input_path
import os
import numpy as np

lines = [line.rstrip().split() for line in open(os.path.join(input_path, "input9.txt")).readlines()]


def task1():
    ans = 0
    for line in lines:
        steps = 0
        triangle = [[int(x) for x in line]]
        while any(triangle[-1]):
            triangle.append(np.subtract(triangle[steps][1:], triangle[steps][:-1]))
            steps += 1
        next_val = 0
        for ind, tri in enumerate(reversed(triangle[:-1]), 0):
            next_val += triangle[ind][-1]
        ans += next_val
    print(f"The answer to part one is {ans}\n")


def task2():
    ans = 0
    for line in lines:
        steps = 0
        triangle = [[int(x) for x in line]]
        while any(triangle[-1]):
            triangle.append(np.subtract(triangle[steps][1:], triangle[steps][:-1]))
            steps += 1
        next_val = 0
        for ind, tri in enumerate(reversed(triangle[:-1]), 0):
            next_val = tri[0] - next_val
        ans += next_val
    print(f"The answer to part two is {ans}")


if __name__ == "__main__":
    task1()
    task2()
