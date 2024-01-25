from config import input_path
import os
import re


def get_input(test: bool):
    if test:
        lines = [line.rstrip() for line in open(os.path.join(input_path, "test_input19.txt")) if (not line.startswith("{")
                                                                                                  and line.rstrip())]
        inputs = [line.rstrip().strip("{").strip("}").split(",") for line in open(os.path.join(input_path, "test_input19.txt")) if line.startswith("{")]
    else:
        lines = [line.rstrip() for line in open(os.path.join(input_path, "input19.txt")) if (not line.startswith("{")
                                                                                             and line.rstrip())]
        inputs = [line.rstrip().strip("{").strip("}").split(",") for line in open(os.path.join(input_path, "input19.txt")) if line.startswith("{")]
    return lines, inputs


def parse_workflows(lines: list) -> dict:
    keys = [line.split("{")[0] for line in lines]
    values = [line.split("{")[1].rstrip("}").split(",") for line in lines]
    return dict(zip(keys, values))


def get_next_name(workflow: list, value: dict):
    for rule in workflow:
        if ":" not in rule:
            return rule
        else:
            match, new_name = rule.split(":")
            cat = re.split("[<>]", match)[0]
            number = int(re.split("[<>]", match)[1])
            if "<" in match and value[cat] < number:
                return new_name
            elif ">" in match and value[cat] > number:
                return new_name


def task1():
    lines, inputs = get_input(False)
    workflows = parse_workflows(lines)
    sums = 0
    for part in inputs:
        part = dict(zip([x.split("=")[0] for x in part], [int(x.split("=")[1]) for x in part]))
        workflow_name = "in"

        while workflow_name not in ["A", "R"]:
            workflow_name = get_next_name(workflows[workflow_name], part)
        if workflow_name == "A":
            sums += sum(part.values())

    print(f"the answer to part one is {sums}\n")


if __name__ == "__main__":
    task1()
