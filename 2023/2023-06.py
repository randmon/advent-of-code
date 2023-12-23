from aocd import get_data

input = get_data(day=6, year=2023).strip().split("\n")
# input = open("test.txt").read().strip().split("\n")


print("\n## Part 1 ##")

times, distances = [list(map(int, x.split(": ")[1].split())) for x in input]
n = 1

for time, dist in zip(times, distances):
    margin = 0
    for hold in range(1, time):
        if hold * (time - hold) > dist:
            margin += 1
    n *= margin

print(n)


print("\n## Part 2 ##")

time = int("".join(input[0].split(": ")[1].split()))
dist = int("".join(input[1].split(": ")[1].split()))

margin = 0
for hold in range(1, time):
    if hold * (time - hold) > dist:
        margin += 1
print(margin)