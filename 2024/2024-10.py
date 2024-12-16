from aocd import get_data
from utils import bcolors
import time

is_example = True

if not is_example: input = get_data(day=10, year=2024).strip().split("\n")
else: input = open("2024/10.in").read().strip().split("\n")

print(bcolors.CLEAR)
print("\n## Part 1 ##")

width = len(input[0])
height = len(input)

map = [["." for _ in range(width)] for _ in range(height)]

def print_map(map):
  print(bcolors.CLEAR)
  for row in map:
    for col in row:
      match col:
        case ".": print(f"{bcolors.BOLD}{col} {bcolors.ENDC}", end="")
        case "0": print(f"{bcolors.BOLD}{bcolors.WARNING}{col} {bcolors.ENDC}", end="")
        case "1": print(f"{bcolors.BOLD}{bcolors.WARNING}{col} {bcolors.ENDC}", end="")
        case "2": print(f"{bcolors.BOLD}{bcolors.OKGREEN}{col} {bcolors.ENDC}", end="")
        case "3": print(f"{bcolors.BOLD}{bcolors.OKGREEN}{col} {bcolors.ENDC}", end="")
        case "4": print(f"{bcolors.BOLD}{bcolors.OKCYAN}{col} {bcolors.ENDC}", end="")
        case "5": print(f"{bcolors.BOLD}{bcolors.OKCYAN}{col} {bcolors.ENDC}", end="")
        case "6": print(f"{bcolors.BOLD}{bcolors.OKBLUE}{col} {bcolors.ENDC}", end="")
        case "7": print(f"{bcolors.BOLD}{bcolors.OKBLUE}{col} {bcolors.ENDC}", end="")
        case "8": print(f"{bcolors.BOLD}{bcolors.HEADER}{col} {bcolors.ENDC}", end="")
        case "9": print(f"{bcolors.BOLD}{bcolors.FAIL}{col} {bcolors.ENDC}", end="")
    print()


paths = []

# Find the starting points
for i in range(height):
  for j in range(width):
    if input[i][j] == "0":
      paths.append([(i, j)])
      map[i][j] = "0"

def get_neighbours(r, c, value):
  neighbours = []
  if r > 0 and input[r-1][c] == value: neighbours.append((r-1, c)) # Up
  if r < height - 1 and input[r+1][c] == value: neighbours.append((r+1, c)) # Down
  if c > 0 and input[r][c-1] == value: neighbours.append((r, c-1)) # Left
  if c < width - 1 and input[r][c+1] == value: neighbours.append((r, c+1)) # Right
  return neighbours

def next_step(paths, value):
  new_paths = []
  for i in range(len(paths)):
    row, col = paths[i][-1]
    neighbours = get_neighbours(row, col, value)
    for neighbour in neighbours:
      n_row, n_col = neighbour
      if input[n_row][n_col] == value and map[n_row][n_col] == ".":
        map[n_row][n_col] = value
        new_paths.append(paths[i] + [(n_row, n_col)])
  return new_paths


for i in range(1, 10):
  print_map(map)
  paths = next_step(paths, str(i))
  time.sleep(0.5)
  
print_map(map)
print("Result:", len(paths))
print("THIS DOES NOT WORK YET")