from aocd import get_data

input = get_data(day=2, year=2023).strip().split("\n")


print("\n## Part 1 ##")

import re

max_cubes = {"red": 12, "green": 13, "blue": 14}

red = re.compile(r"(\d+) red")
green = re.compile(r"(\d+) green")
blue = re.compile(r"(\d+) blue")

possible_games = []
for i, line in enumerate(input):
    red_matches = red.findall(line)
    if len(red_matches) != 0:
        red_max = max([int(x) for x in red_matches])
        if red_max > max_cubes["red"]:
            continue
        
    green_matches = green.findall(line)
    if len(green_matches) != 0:
        green_max = max([int(x) for x in green_matches])
        if green_max > max_cubes["green"]:
            continue

    blue_matches = blue.findall(line)
    if len(blue_matches) != 0:
        blue_max = max([int(x) for x in blue_matches])
        if blue_max > max_cubes["blue"]:
            continue

    possible_games.append(i+1)
print(sum(possible_games))


print("\n## Part 2 ##")

total = 0

for line in input:
    red_matches = red.findall(line)
    red_max = 0
    if len(red_matches) != 0:
        red_max = max([int(x) for x in red_matches])

    green_matches = green.findall(line)
    green_max = 0
    if len(green_matches) != 0:
        green_max = max([int(x) for x in green_matches])

    blue_matches = blue.findall(line)
    blue_max = 0
    if len(blue_matches) != 0:
        blue_max = max([int(x) for x in blue_matches])

    powers = red_max * green_max * blue_max
    total += powers

print(total)
