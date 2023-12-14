from config import input_path
import os


with open(os.path.join(input_path, 'input5.txt'), 'r') as file:
    lines = file.readlines()
    # print(lines[1:])

seed_list = lines[0].split(":")[1].split()


def get_location(seed):
    map_indices = [ind + 1 for ind, line in enumerate(lines) if 'map:' in line]
    map_indices.append(len(lines) + 2)
    dest = seed
    for map_index in range(7):
        for i in range(map_indices[map_index], map_indices[map_index + 1] - 2):
            dest_start, source_start, range_len = lines[i].split()
            if dest in range(int(source_start), int(source_start) + int(range_len)):
                dest = dest - int(source_start) + int(dest_start)
                break
    return dest


def task1():
    locations = []
    for seed in seed_list:
        locations.append(get_location(int(seed)))
    print(f"The lowest location number is {min(locations)}\n")


def task2():
    locations = []
    seed_start = [int(seed_list[2*ind]) for ind in range(int(len(seed_list)/2))]
    seed_range = [int(seed_list[2*ind + 1]) for ind in range(int(len(seed_list)/2))]
    for ind, seed_starts in enumerate(seed_start):
        print(f"Starting seed number {ind + 1}")
        for seed in range(seed_starts, seed_starts + seed_range[ind]):
            locations.append(get_location(seed))

    print(f"The lowest location number is {min(locations)}")


if __name__ == "__main__":
    # task1()
    task2()
