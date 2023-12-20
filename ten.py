import sys

from config import input_path
import numpy as np
import math
import os

lines = [line.rstrip() for line in open(os.path.join(input_path, "input10.txt"))]

# pipes = np.array([list(x) for x in ['.....', '.S-7.', '.|.|.', '.L-J.', '.....']])
pipes = np.array([list(x) for x in lines])
dist = np.ones(np.shape(pipes)) * np.inf
# print(dist)

start_node = np.argwhere(pipes == "S")[0]
dist[tuple(start_node)] = 0

chars = {"|": ("north", "south"), "-": ("east", "west"), "L": ("north", "east"), "J": ("north", "west"),
         "7": ("south", "west"), "F": ("south", "east"), ".": ""}

dirs = {"north": np.array((-1, 0)), "east": np.array((0, 1)), "south": np.array((1, 0)), "west": np.array((0, -1))}

opp_dirs = {"north": "south", "south": "north", "east": "west", "west": "east"}


def make_dist_map():
    current_node = start_node
    start_dir = []
    for direction in ["north", "east", "south", "west"]:
        if opp_dirs[direction] in chars[pipes[tuple(current_node + dirs[direction])]]:
            start_dir.append(direction)
    for new_dir in start_dir:
        current_node = start_node
        new_node = current_node + dirs[new_dir]
        dist[tuple(new_node)] = dist[tuple(current_node)] + 1

        while True:

            new_node = current_node + dirs[new_dir]
            if pipes[tuple(new_node)] == "S":
                break

            dist[tuple(new_node)] = min(dist[tuple(current_node)] + 1, dist[tuple(new_node)])
            new_char = pipes[tuple(new_node)]
            new_dir = [x for x in chars[new_char] if x != opp_dirs[new_dir]][0]
            current_node = new_node

    return dist


def task1():
    dist_map = make_dist_map()
    print(f"The answer to part one is {int(np.nanmax(np.ma.where(dist_map != np.inf, dist_map, np.nan)))}\n")


def task2():
    
    return


if __name__ == "__main__":
    task1()
