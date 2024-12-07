from aocd import get_data

input = get_data(day=5, year=2024).strip().split("\n\n")
# input = open("test.txt").read().strip().split("\n\n")

pages_order = [i.split("|") for i in input[0].split("\n")]
updates = [i.split(",") for i in input[1].split("\n")]

print("\n## Part 1 ##")

pages_map = {}
for p in pages_order:
  pages_map.setdefault(p[0], []).append(p[1])

incorrect_fixed = []

# Fix the order of the pages in the update list, according to the pages_map.
def fix_update(update):
  for i in range(len(update)):
    current = update[i]
    if current not in pages_map:
      continue
    # Look at all the pages before the current one,
    # and if they were not supposed to be printed before, swap them.
    for j in range(i):
      if update[j] in pages_map[current]:
        update[i], update[j] = update[j], update[i]
  return update

def check_update(update):
  for i in range(len(update)):
    current = update[i]
    if current not in pages_map:
      continue
    # Look at all the pages before the current one,
    # and if they were not supposed to be printed before, increment the counter.
    for j in range(i):
      if update[j] in pages_map[current]:
        incorrect_fixed.append(fix_update(update))
        return False
  return True

  
def add_middle_numbers(ns):
  return sum([int(n[len(n) // 2]) for n in ns])

correct = []
for u in updates:
  if check_update(u):
    correct.append(u)

print(add_middle_numbers(correct))

print("\n## Part 2 ##")

print(add_middle_numbers(incorrect_fixed))
