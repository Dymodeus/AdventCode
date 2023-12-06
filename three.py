from config import input_path
import re
import os

with open(os.path.join(input_path, "input3.txt"), "r") as file:
    lines = file.readlines()

numbers = []

for ind, line in enumerate(lines):
    numbers.append([(int(m[0]), m.span()) for m in re.finditer(r"\d+", line)])


def check_for_chars(x1, x2, y1, y2):
    flag = False
    for ind1 in range(x1, x2 + 1):
        for ind2 in range(y1, y2 + 1):
            print(ind1, ind2)
    return flag


# check first row
for ind, line in enumerate(numbers):
    check_for_chars(1, 2, 1, 2)
