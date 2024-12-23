from aocd import get_data
from utils import bcolors
import itertools

is_example = False

if not is_example: input = get_data(day=8, year=2024).strip().split("\n")
else: input = open("2024/8.in").read().strip().split("\n")

print(bcolors.CLEAR)
print("\n## Part 1 ##\n")

if is_example:
  for i in input: print(i)
width = len(input[0])
height = len(input)
    
def get_anti_nodes(a1, a2):
  x1, y1 = a1
  x2, y2 = a2
  
  # First antinode
  diff_x = x1 - x2
  diff_y = y1 - y2
  x3 = x1 + diff_x
  y3 = y1 + diff_y
  
  if is_example: print(f"Diff: x= {diff_x} | y= {diff_y}")
  
  # Second antinode
  diff_x = x2 - x1
  diff_y = y2 - y1
  x4 = x2 + diff_x
  y4 = y2 + diff_y

  if is_example: print(f"Diff: x= {diff_x} | y= {diff_y}")
  return (x3, y3), (x4, y4)
  
      

antennas = {}
for row_num, row in enumerate(input):
  for col_num, c in enumerate(row):
    if c != ".":
      antennas.setdefault(c, []).append((row_num, col_num))
  
result = []
   
for group in antennas:
  if is_example: print(f"\n{bcolors.BLUE}--- {group} ---{bcolors.ENDC}")
  all_combinations = list(itertools.combinations(antennas[group], 2))
  for a, b in all_combinations:
    if is_example: print(f"\n{bcolors.GREEN}--- {a} {b} ---{bcolors.ENDC}")
    a1, a2 = get_anti_nodes(a, b)
    if is_example: print(f"Antinodes: {a1} {a2}")
    if a1[0] >= 0 and a1[0] < height and a1[1] >= 0 and a1[1] < width:
      if result.count(a1) == 0:
        result.append(a1)
    if a2[0] >= 0 and a2[0] < height and a2[1] >= 0 and a2[1] < width:
      if result.count(a2) == 0:
        result.append(a2)

print(len(result))
  
  
def print_board():
  for row_num, row in enumerate(input):
    for col_num, c in enumerate(row):
      if (row_num, col_num) in result:
        if c == ".":
          print(f"{bcolors.CYAN}{bcolors.BOLD}#{bcolors.ENDC}", end="")
        else:
          print(f"{bcolors.GREEN}{bcolors.BOLD}{c}{bcolors.ENDC}", end="")
      elif c != ".":
        print(f"{bcolors.YELLOW}{bcolors.BOLD}{c}{bcolors.ENDC}", end="")
      else:
        print(c, end="")
    print()

if is_example: print_board()

print("\n## Part 2 ##\n")

def get_more_antinodes(a1, a2):
  x1, y1 = a1
  x2, y2 = a2
  
  result = []
  
  # First direction
  diff_x = x1 - x2
  diff_y = y1 - y2
  
  x3 = x1
  y3 = y1
  
  while(True):
    x3 = x3 + diff_x
    y3 = y3 + diff_y
    if x3 < 0 or x3 >= height or y3 < 0 or y3 >= width:
      break
    result.append((x3, y3))
  
  # Second antinode
  diff_x = x2 - x1
  diff_y = y2 - y1
  
  x3 = x2
  y3 = y2
  
  while(True):
    x3 = x3 + diff_x
    y3 = y3 + diff_y
    if x3 < 0 or x3 >= height or y3 < 0 or y3 >= width:
      break
    result.append((x3, y3))
    
  return result

result = [a for group in antennas for a in antennas[group]]

for group in antennas:
  if is_example: print(f"\n{bcolors.BLUE}--- {group} ---{bcolors.ENDC}")
  all_combinations = list(itertools.combinations(antennas[group], 2))
  for a, b in all_combinations:
    if is_example: print(f"\n{bcolors.GREEN}--- {a} {b} ---{bcolors.ENDC}")
    nodes = get_more_antinodes(a, b)
    if is_example: print(f"Antinodes: {nodes}")
    for node in nodes:
      if result.count(node) == 0 and node not in antennas[group]:
        result.append(node)

print(len(result))
if is_example: print_board()