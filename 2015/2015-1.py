from aocd import get_data

input = get_data(day=1, year=2015)

print("\n## Part 1 ##")

print(input.count('(') - input.count(')'))

print("\n## Part 2 ##")

floor = 0
for i, char in enumerate(input):
    floor += 1 if char == '(' else -1
    if floor == -1:
        print(i + 1)
        break
