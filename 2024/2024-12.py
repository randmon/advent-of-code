from aocd import get_data
from utils import bcolors, start_timer, print_timer
from collections import deque

is_example = False

if not is_example: grid = get_data(day=12, year=2024).strip().split("\n")
else: grid = open("2024/12.in").read().strip().split("\n")

grid = [list(i) for i in grid]

print(bcolors.CLEAR)
print("\n## Part 1 ##")
start_timer()

rows = len(grid)
cols = len(grid[0])

regions = []
seen = set()

for r in range(rows):
  for c in range(cols):
    if (r, c) in seen: continue
    seen.add((r, c))
    region = {(r, c)}
    q = deque([(r, c)])
    crop = grid[r][c]
    while q:
      cr, cc = q.popleft()
      for nr, nc in [(cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)]:
        if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
        this_crop = grid[nr][nc]
        if this_crop != crop: continue
        if (nr, nc) in region: continue
        region.add((nr, nc))
        q.append((nr, nc))
    seen |= region
    regions.append(region)
    
def perimeter(region):
  output = 0
  for (r, c) in region:
    output += 4
    for nr, nc in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
      if (nr, nc) in region:
        output -= 1
  return output

if is_example:
  for i in range(len(regions)):
    region = regions[i]
    r, c = next(iter(region))
    crop = grid[r][c]
    a = len(region)
    s = perimeter(region)
    print(f"- A region of {bcolors.BOLD}{crop}{bcolors.ENDC} plants with price {bcolors.BOLD}{a} * {s} = {a * s}{bcolors.ENDC}")

print(sum(len(region) * perimeter(region) for region in regions))

print_timer()


print("\n## Part 2 ##")
start_timer()

def sides(region):
  corner_candidates = set()
  for r, c in region:
    for cr, cc in [(r-0.5, c-0.5), (r+0.5, c-0.5), (r+0.5, c+0.5), (r-0.5, c+0.5)]:
      corner_candidates.add((cr, cc))
  corners = 0
  for cr, cc in corner_candidates:
    config = [(sr, sc) in region for sr, sc in[(cr-0.5, cc-0.5), (cr+0.5, cc-0.5), (cr+0.5, cc+0.5), (cr-0.5, cc+0.5)]]
    number = sum(config)
    if number == 1 or number == 3: corners += 1
    elif number == 2 and (config == [True, False, True, False] or config == [False, True, False, True]): corners += 2
  return corners

if is_example:
  for i in range(len(regions)):
    region = regions[i]
    r, c = next(iter(region))
    crop = grid[r][c]
    a = len(region)
    s = sides(region)
    print(f"- A region of {bcolors.BOLD}{crop}{bcolors.ENDC} plants with price {bcolors.BOLD}{a} * {s} = {a * s}{bcolors.ENDC}")

print(sum(len(region) * sides(region) for region in regions))

print_timer()