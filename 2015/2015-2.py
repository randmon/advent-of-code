from aocd import get_data

input = get_data(day=2, year=2015).split("\n")
presents = [present.split("x") for present in input]
presents = [[int(dimension) for dimension in present] for present in presents]

print("\n## Part 1 ##")

result = 0

for p in presents:
    sides = [p[0] * p[1], p[0] * p[2], p[1] * p[2]]
    smallest = min(sides)
    total = 2 * sum(sides) + smallest
    result += total

print(result)

print("\n## Part 2 ##")

result = 0

for p in presents:
    perimeters = [p[0] + p[1], p[0] + p[2], p[1] + p[2]]
    smallest = min(perimeters)
    volume = p[0] * p[1] * p[2]
    total = (2 * smallest) + volume
    result += total

result

print(result)