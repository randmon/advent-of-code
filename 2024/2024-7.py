from aocd import get_data

is_example = True

if not is_example: input = get_data(day=7, year=2024).strip().split("\n")
else: input = open("2024/7.in").read().strip().split("\n")

print("\n## Part 1 ##")

for i in input: print(i)