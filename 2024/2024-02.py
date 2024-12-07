from aocd import get_data

input = get_data(day=2, year=2024).strip().split("\n")
# input = open("test.txt").read().strip().split("\n")

print("\n## Part 1 ##")

def is_increasing(ns):
  for i in range(len(ns) - 1):
    if ns[i] >= ns[i + 1]:
      return False
  return True

def is_decreasing(ns):
  for i in range(len(ns) - 1):
    if ns[i] <= ns[i + 1]:
      return False
  return True

def safe_distances(ns):
  for i in range(len(ns) - 1):
    distance = abs(ns[i] - ns[i + 1])
    if distance < 1 or distance > 3:
      return False
  return True

input = [a.split() for a in input]
input = [[int(a) for a in b] for b in input]

result = 0

for row in input:
  if (is_increasing(row) or is_decreasing(row)) and safe_distances(row):
    result += 1
    
print(result)


print("\n## Part 2 ##")

def problem_dampener(ns):
  # First try the full list
  for row in ns:
    if (is_increasing(ns) or is_decreasing(ns)) and safe_distances(ns):
      return True
  
  # Then try removing one element
  for i in range(len(ns)):
    row = ns[:i] + ns[i+1:]
    if (is_increasing(row) or is_decreasing(row)) and safe_distances(row):
      return True
  
  return False

result = 0

for row in input:
  if problem_dampener(row):
    result += 1
    
print(result)