from aocd import get_data
from utils import bcolors
from collections import deque

is_example = True

if not is_example: input = get_data(day=10, year=2024).strip().split("\n")
else: input = open("2024/10.in").read().strip().split("\n")

print(bcolors.CLEAR)
print("\n## Part 1 ##")

input = [[int(cell) for cell in row] for row in input]
width = len(input[0])
height = len(input)

trail_heads = [(row, col) for row in range(height) for col in range(width) if input[row][col] == 0]

def score(grid, row, col):
  assert grid[row][col] == 0
  path = deque([(row, col)])
  seen = {(row, col)}
  summits = 0
  
  while len(path) > 0:
    curr_row, curr_col = path.popleft()
    for nr, nc in [(curr_row-1, curr_col), 
                   (curr_row+1, curr_col), 
                   (curr_row, curr_col-1), 
                   (curr_row, curr_col+1)]:
      
      # If out of bounds, skip
      if nr < 0 or nr >= height or nc < 0 or nc >= width: continue
      # If not a +1 step, skip
      if grid[nr][nc] != grid[curr_row][curr_col] + 1: continue
      # If already seen, skip
      if (nr, nc) in seen: continue
      seen.add((nr, nc))
      
      # If is summit
      if grid[nr][nc] == 9: summits += 1
      else: path.append((nr, nc))
      
  return summits
  
result = sum([score(input, row, col) for row, col in trail_heads])
print(result)