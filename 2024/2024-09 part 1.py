from aocd import get_data
from utils import bcolors
import time

is_example = True

if not is_example: input = get_data(day=9, year=2024).strip()
else: input = open("2024/9.in").read().strip()

print(bcolors.CLEAR)
print("\n## Part 1 ##")

system = []

id = 0

for i, char in enumerate(input):
  if i % 2 != 0:
    system.extend([-1] * int(char))
  else:
    system.extend([id] * int(char))
    id += 1
    
original_system = system.copy()

def print_system(system):
  for i in system:
    if i == -1:
      print(f"{bcolors.BOLD}{bcolors.YELLOW}. {bcolors.ENDC}", end="")
    else:
      print(f"{bcolors.BOLD}{bcolors.GREEN}{i} {bcolors.ENDC}", end="")
  print()
   
if is_example: print_system(system)

for i in range(len(system)-1, 0, -1):
  if system[i] == -1:
    continue
  else:
    try:
      next_empty = system.index(-1, 0, i)
      if is_example:
        print(f"{bcolors.CLEAR}Original system:")
        print_system(original_system)
        print(f"\n\nMoving {system[i]} to {next_empty}")
      
      system[next_empty] = system[i]
      system[i] = -1
      if is_example:
        print_system(system)
        time.sleep(0.2)
    except ValueError:
      break
  
if is_example:
  print(f"{bcolors.CLEAR}Original system:")
  print_system(original_system)
  print(f"\n\nOptimization complete!")
  print_system(system)

result = 0
for i in range(len(system)):
  if system[i] == -1:
    break
  result += system[i] * (i)

print(f"\nResult: {result}")
if is_example: assert result == 1928