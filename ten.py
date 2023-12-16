from config import input_path
import os

lines = [line.rstrip() for line in open(os.path.join(input_path, "input10.txt"))]
print(lines)
