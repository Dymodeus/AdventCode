from config import input_path
import os

with open(os.path.join(input_path, "input15.txt")) as file:
    line = file.readline().rstrip().split(",")

test_line = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")


def hashing(step: str):
    curr_val = 0
    for char in list(step):
        curr_val += ord(char)
        curr_val *= 17
        curr_val = curr_val % 256
    return curr_val


def task1():
    sum_of_ascii = 0
    for step in line:
        sum_of_ascii += hashing(step)
    print(f"The answer to part one is {sum_of_ascii}\n")


def task2():
    list_of_boxes = []
    for i in range(256):
        list_of_boxes.append([])
    for step in test_line:
        # print(list_of_boxes)
        if "=" in step:
            label = step.split("=")[0]
            box_nr = hashing(label)
            print(box_nr)
            replaced = False
            for ind, content in enumerate(list_of_boxes[box_nr]):
                if label in content:
                    list_of_boxes[box_nr][ind] = step.replace("=", " ")
                    replaced = True
            if not replaced:
                list_of_boxes[box_nr].append(step.replace("=", " "))
        elif "-" in step:
            label = step[:-1]
            box_nr = hashing(label)
            for ind, content in enumerate(list_of_boxes[box_nr]):
                if label in content:
                    list_of_boxes[box_nr].pop(ind)
        else:
            break
    print(list_of_boxes)
    sum_of_focus = 0
    for ind_box, box in enumerate(list_of_boxes, 1):
        for slot, lens in enumerate(box, 1):
            power = ind_box * slot * int(lens.split()[1])
            sum_of_focus += power
    print(f"The answer to part two is {sum_of_focus}\n")


if __name__ == "__main__":
    # task1()
    task2()
