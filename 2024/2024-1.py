from aocd import get_data

input = get_data(day=1, year=2024).strip().split("\n")
# input = open("test.txt").read().strip().split("\n")

print("\n## Part 1 ##")

left = []
right = []

for pair in input:
  l, r = map(int, pair.split())
  left.append(l)
  right.append(r)

pairs = zip(sorted(left), sorted(right))
result = sum([abs(l - r) for l, r in pairs])

print(result)

print("\n## Part 2 ##")

# Make a map of how many times each number appears in the right list
right_map = {r: right.count(r) for r in right}
  
# For each number in the left list, 
# multiply it by the nymer of times it appears in the right list
result = sum([l * right_map.get(l, 0) for l in left])
print(result)
