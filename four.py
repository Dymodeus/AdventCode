from config import input_path
import os


def parse_input():
    with open(os.path.join(input_path, "input4.txt")) as file:
        lines = file.readlines()

    return table_of_winners, table_of_entries


def task1():
    sum_of_points = 0

    return sum_of_points