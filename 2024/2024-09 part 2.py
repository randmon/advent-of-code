from aocd import get_data
from utils import bcolors
import time

is_example = False

if not is_example: input = get_data(day=9, year=2024).strip()
else: input = open("2024/9.in").read().strip()

print(bcolors.CLEAR)
print("\n## Part 2 ##")

system = []

id = 0

for i, char in enumerate(input):
  if i % 2 != 0:
    if char != "0":
      system.append((-1, int(char)))
  else:
    system.append((id, int(char)))
    id += 1
    
original_system = system.copy()

def print_system(system):
  for i in system:
    if i[0] == -1:
      c = ". "*i[1]
      print(f"{bcolors.BOLD}{bcolors.WARNING}{c}{bcolors.ENDC}", end="")
    else:
      c = f"{i[0]} "*i[1]
      print(f"{bcolors.BOLD}{bcolors.OKGREEN}{c}{bcolors.ENDC}", end="")
  print()
   
if is_example: print_system(system)

def find_next_empty(system, end, min_width):
  for i in range(0, end):
    if system[i][0] == -1 and system[i][1] >= min_width:
      return i
  return -1

current_i = len(system)-1

while current_i > 0:
  current = system[current_i]
  
  if current[0] == -1:
    current_i -= 1
    continue
  else:
    next_empty = find_next_empty(system, current_i, current[1])
    
    if next_empty == -1:
      current_i -= 1
      continue
    
    if is_example:
      print(f"{bcolors.CLEAR}Original system:")
      print_system(original_system)
      print(f"\n\nMoving {system[current_i][0]} to {next_empty}")
    
    empty = system[next_empty]
    system[next_empty] = current
    
    # The block moved leaves behind an empty space
    system[current_i] = (-1, current[1])
    
    if empty[1] > current[1]:
      # Append the rest of the empty space between the added block and the next block
      system.insert(next_empty+1, (-1, empty[1] - current[1]))
      current_i += 1
    
    if is_example:
      print_system(system)
      time.sleep(0.5)
      
  current_i -= 1
    
    
  
if is_example:
  print(f"{bcolors.CLEAR}Original system:")
  print_system(original_system)
  print(f"\n\nOptimization complete!")
  print_system(system)

def calc_checksum(system):
  result = 0
  index = 0
  for i in range(len(system)):
    if system[i][0] == -1:
      index += system[i][1]
      continue
    for _ in range(system[i][1]):
      result += system[i][0] * index
      index += 1
    
  return result

result = calc_checksum(system)
print(f"\nResult: {result}")
if is_example: assert result == 2858