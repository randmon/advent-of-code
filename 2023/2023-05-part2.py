# solution from https://www.youtube.com/watch?v=_RpZrD3CaDc because i could not figure this out for the life of me
from aocd import get_data
print("\n## Part 2 ##")

input = get_data(day=5, year=2023).strip().split("\n")
# input = open("test.txt").read().strip().split("\n")

seeds_input = list(map(int, input[0].split()[1:]))
seeds = [(seeds_input[i], seeds_input[i+1]) for i in range(0, len(seeds_input), 2)]

mappings = []

i = 2
while i < len(input):
    catA, _, catB = input[i].split(" ")[0].split("-")
    mapping = []
    
    i += 1
    while i < len(input) and input[i]:
        dstStart, srcStart, rangeLen = map(int, input[i].split())
        mapping.append((dstStart, srcStart, rangeLen))
        i += 1

    mapping.sort(key=lambda x: x[1])
    mappings.append(mapping)
    i += 1

def remap(interval, m):
    low, high = interval
    ans = []
    
    for destination, source, range in m:
        end = source + range - 1
        diff = destination - source

        if not (end < low or source > high):
            ans.append((max(source, low), min(end, high), diff))

    for i, interval in enumerate(ans):
        left, right, diff = interval
        yield (left + diff, right + diff)

        if i < len(ans) - 1 and ans[i+1][0] > right + 1:
            yield (right + 1, ans[i+1][0] - 1)

    if len(ans) == 0:
        yield (low, high)
        return

    if ans[0][0] != low:
        yield (low, ans[0][0] - 1)
    if ans[-1][1] != high:
        yield (ans[-1][1] + 1, high)


min_location = float("inf")

for seed_start, range in seeds:
    cur_intervals = [(seed_start, seed_start + range - 1)]
    new_intervals = []

    for m in mappings:
        for interval in cur_intervals:
            for new_interval in remap(interval, m):
                new_intervals.append(new_interval)

        cur_intervals, new_intervals = new_intervals, []

    for low, _ in cur_intervals:
        min_location = min(min_location, low)

print(min_location)