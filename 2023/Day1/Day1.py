import os
from utils.ReadFile import readfile

def solve_1(input_str: str) -> int:
    lines = input_str.split(sep="\n")
    digits = [[c for c in line if c.isdigit()] for line in lines]
    digits = [digit[0] + digit[-1] for digit in digits]
    total = [int(digit) for digit in digits]
    return sum(total)


def solve_2(input_str: str) -> int:
    needles = ["one","two","three","four","five","six","seven","eight","nine","0","1","2","3","4","5","6","7","8","9"]
    needles_reversed = [needle[::-1] for needle in needles]
    num = []
    for line in input_str.split(sep="\n"):
        left = [(needle, line.index(needle)) for needle in needles if needle in line]
        leftNum = min(left, key=lambda x : x[1])
        leftIndex = needles.index(leftNum[0]) + 10 if needles.index(leftNum[0]) <= 8 else needles.index(leftNum[0])


        right = [(needle, line[::-1].index(needle)) for needle in needles_reversed if needle in line[::-1]]
        rightNum = min(right, key=lambda x : x[1])
        rightIndex = needles.index(rightNum[0][::-1]) + 10 if needles.index(rightNum[0][::-1]) <= 8 else needles.index(rightNum[0][::-1])

        num.append(int(needles[leftIndex] + needles[rightIndex]))
    return sum(num)

    
    
input_str = readfile(os.path.join(os.path.dirname(__file__), "sample.txt"))
assert solve_1(input_str) == 142
input_str = readfile(os.path.join(os.path.dirname(__file__), "input.txt"))
assert solve_1(input_str) == 55029

input_str = readfile(os.path.join(os.path.dirname(__file__), "sample2.txt"))
assert solve_2(input_str) == 281
input_str = readfile(os.path.join(os.path.dirname(__file__), "input.txt"))
assert solve_2(input_str) == 55686
