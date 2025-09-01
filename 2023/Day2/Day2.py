import os
import re
import sys
from utils.utils import is_eq, readfile

limits = {"red": 12, "green": 13, "blue": 14}


def solve_1(input_str: str) -> int:
    r = 0
    for line in input_str.splitlines():
        game_id = int(line.split(":")[0].split("Game ")[1])
        game_sets = list(map(str.strip, line.split(":")[1].split(";")))
        is_valid = True
        for game_set in game_sets:
            balls = list(map(str.strip, game_set.split(",")))
            for ball in balls:
                ball_color = ball.split(" ")[1]
                ball_count = int(ball.split(" ")[0])
                if ball_count > limits[ball_color]:
                    is_valid = False
                    break
            if not is_valid:
                break

        if is_valid:
            r += game_id
    return r


def solve_2(input_str: str) -> int:
    r = 0
    for line in input_str.splitlines():
        game_sets = list(map(str.strip, line.split(":")[1].split(";")))
        game_balls_min: dict[str, int] = dict(red=0, green=0, blue=0)
        for game_set in game_sets:
            balls = list(map(str.strip, game_set.split(",")))
            for ball in balls:
                ball_color = ball.split(" ")[1]
                ball_count = int(ball.split(" ")[0])
                if ball_count > game_balls_min[ball_color]:
                    game_balls_min[ball_color] = ball_count
        r += game_balls_min["red"] * game_balls_min["green"] * game_balls_min["blue"]
    return r


input_str = readfile(os.path.join(os.path.dirname(__file__), "sample.txt"))
is_eq(solve_1(input_str), 8)
input_str = readfile(os.path.join(os.path.dirname(__file__), "input.txt"))
is_eq(solve_1(input_str), 2679)

input_str = readfile(os.path.join(os.path.dirname(__file__), "sample.txt"))
is_eq(solve_2(input_str), 2286)
input_str = readfile(os.path.join(os.path.dirname(__file__), "input.txt"))
is_eq(solve_2(input_str), 77607)
