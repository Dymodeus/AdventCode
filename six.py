from config import input_path
import os


with open(os.path.join(input_path, "input6.txt"), "r") as file:
    lines = file.readlines()
    times = lines[0].split(':')[1].split()
    dist = lines[1].split(':')[1].split()


def amount_of_records(dist, time):
    distance_per_race = []
    for hold in range(time):
        distance_per_race.append(hold * (time - hold))
    return len([x for x in distance_per_race if x > dist]), distance_per_race


def task1():
    ans = 1
    for ind in range(len(times)):
        ans *= amount_of_records(int(dist[ind]), int(times[ind]))[0]
    print(f"The answer to part one is {ans}\n")


if __name__ == "__main__":
    task1()
