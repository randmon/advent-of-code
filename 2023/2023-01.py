from aocd import get_data

input = get_data(day=1, year=2023).strip().split("\n")


print("\n## Part 1 ##")

numbers = []

for line in input:
    digits = [char for char in line if char.isdigit()]
    numbers.append(int("".join([digits[0], digits[-1]])))

print(sum(numbers))


print("\n## Part 2 ##")

import re

numberDict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

reversedNumberDict = {k[::-1]:v for k, v in numberDict.items()}

def findFirstNumber(string):
    pattern = r"\d|one|two|three|four|five|six|seven|eight|nine"
    match = re.search(pattern, string).group()
    if match.isdigit():
        return match
    else:
        return numberDict[match]

def findLastNumber(string):
    pattern = r"\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin"
    match = re.search(pattern, string[::-1]).group()
    if match.isdigit():
        return match
    else:
        return reversedNumberDict[match]

total = 0
for line in input:
    total += int(findFirstNumber(line))*10 + int(findLastNumber(line))

print(total)
