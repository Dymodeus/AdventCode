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

current_node = start_node
start_dir = []
for direction in ["north", "east", "south", "west"]:
    if opp_dirs[direction] in chars[pipes[tuple(current_node + dirs[direction])]]:
        start_dir.append(direction)
print(start_dir)
for new_dir in start_dir:
    current_node = start_node
    new_node = current_node + dirs[new_dir]
    new_char = pipes[tuple(new_node)]
    dist[tuple(new_node)] = dist[tuple(current_node)] + 1

    while True:

        new_node = current_node + dirs[new_dir]
        if pipes[tuple(new_node)] == "S":
            break

        dist[tuple(new_node)] = min(dist[tuple(current_node)] + 1, dist[tuple(new_node)])
        new_char = pipes[tuple(new_node)]
        new_dir = [x for x in chars[new_char] if x != opp_dirs[new_dir]][0]
        current_node = new_node
    # print(dist[start_node[0]-2:start_node[0]+3, start_node[1]-2:start_node[1]+3])

# print(dist[start_node[0]-2:start_node[0]+3, start_node[1]-2:start_node[1]+3])
print(np.nanmax(np.ma.where(dist != np.inf, dist, np.nan)))
