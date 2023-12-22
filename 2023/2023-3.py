from aocd import get_data

input = get_data(day=3, year=2023).strip().split("\n")

print("\n## Part 1 ##")

import re

total = 0

def get_all_adjacent_chars(from_x, to_x, from_y, to_y):
    adjacent = []
    for y in range(from_y, to_y+1):
        for x in range(from_x, to_x+1):
            adjacent.append(input[y][x])
    return adjacent
        
for i, line in enumerate(input):
    max_x = len(line)-1
    max_y = len(input)-1
    
    # Find all numbers and their starting and ending positions
    numbers = [(m.start(0), m.end(0), int(m.group(0))) for m in re.finditer(r"\d+", line)]

    for number in numbers:
        # Get all adjacent characters
        from_x = max(0, number[0] - 1)
        to_x = min(max_x, number[1])
        from_y = max(0, i - 1)
        to_y = min(max_y, i + 1)
        adjacent = ''.join(get_all_adjacent_chars(from_x, to_x, from_y, to_y))
        
        # If adjacent contains a symbol, add the number to the total
        r = re.compile(r"[^\d.]") # regex for not a number or a period
        if r.search(adjacent):
            total += number[2]

print(total)


print("\n## Part 2 ##")

gears_with_numbers = {}

def get_all_adjacent_gears(from_x, to_x, from_y, to_y):
        adjacent_gears = [] # a gear will be a tuple of its coordinates
        # adjacent_gears = [(x, y) for y in range(from_y, to_y+1) for x in range(from_x, to_x+1) if input[y][x] == "*"]
        
        for y in range(from_y, to_y+1):
            for x in range(from_x, to_x+1):
                if input[y][x] == "*":
                    adjacent_gears.append((x, y))
                    
        return adjacent_gears

for i, line in enumerate(input):
    max_x = len(line)-1
    max_y = len(input)-1
    
    # Find all numbers and their starting and ending positions
    numbers = [(m.start(0), m.end(0), int(m.group(0))) for m in re.finditer(r"\d+", line)]

    for number in numbers:
        # Get all adjacent characters
        from_x = max(0, number[0] - 1)
        to_x = min(max_x, number[1])
        from_y = max(0, i - 1)
        to_y = min(max_y, i + 1)

        adjacent_gears = get_all_adjacent_gears(from_x, to_x, from_y, to_y)
        for gear in adjacent_gears:
            if gear not in gears_with_numbers:
                gears_with_numbers[gear] = []
            gears_with_numbers[gear].append(number)

gear_ratio_total = 0
        
for gear in gears_with_numbers:
    if len(gears_with_numbers[gear]) == 2: 
        gear_ratio_total += gears_with_numbers[gear][0][2] * gears_with_numbers[gear][1][2]
        
print(gear_ratio_total)