from aocd import get_data
from utils import bcolors, start_timer, print_timer
import time
import math

is_example = False

if not is_example: stones = get_data(day=11, year=2024).split()
else: stones = "125 17".split()

print(bcolors.CLEAR)
print("\n## Part 1 ##")
start_timer()

def num_len(num): return int(math.log10(num)) + 1

seen = {}

def blink(stone):
  if stone == 0: return [1]
  
  if stone in seen: return seen[stone]
  
  len_stone = num_len(stone)
  if len_stone % 2 == 0:
    p = 10 ** (len_stone / 2)
    r = [int(stone / p) , int(stone % p)]
    seen[stone] = r
    return r
  
  else:
    r = [stone * 2024]
    seen[stone] = r
    return r

stones = {int(stone) : 1 for stone in stones}

def get_sum(stones, turns):
  for i in range(1, turns+1):
    if is_example: print(f"Turn {i}: ", end="")
    new_stones = {}
    for stone, stone_count in stones.items():
      blinked = blink(stone)
      for new_stone in blinked:
        if new_stone in new_stones:
          new_stones[new_stone] += stone_count
        else:
          new_stones[new_stone] = stones[stone]
    stones = new_stones
  
    if is_example: print(sum(stones.values()))
    
  return sum(stones.values())
  
result = get_sum(stones, 25)
print(result)
print_timer()


print("\n## Part 2 ##")
start_timer()

result = get_sum(stones, 75)
print(result)
print_timer()