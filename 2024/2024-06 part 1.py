from aocd import get_data
import time

is_example = False

if is_example: input = get_data(day=6, year=2024).strip().split("\n")
else: input = open("2024/6.in").read().strip().split("\n")

print("\n## Part 1 ##")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_board(board):
  # Clear the terminal
  print("\033c")
  
  print()
  for i in board:
    for j in i:
      if j == obstacle:
        print(bcolors.FAIL,bcolors.BOLD + j + bcolors.ENDC, end="")
      elif j in guard_pos:
        print(bcolors.OKBLUE,bcolors.BOLD + j + bcolors.ENDC, end="")
      elif j in [walked_UD, walked_LR, walked_ALL]:
        print(bcolors.OKGREEN,bcolors.BOLD + j + bcolors.ENDC, end="")
      else:
        print(bcolors.WARNING,bcolors.BOLD + j + bcolors.ENDC, end="")
    print()
  print()

  
guard_pos = ["^", ">", "v", "<"]
walked_UD = "|"
walked_LR = "-"
walked_ALL = "+"
obstacle = "#"

def find_guard(input):
  for i in range(len(input)):
    for j in range(len(input[i])):
      if input[i][j] in guard_pos:
        return (input[i][j], i, j)

board1 = [list(i) for i in input]
guard = find_guard(input)

if is_example: print_board(board1)
if is_example: print("Guard:", guard, "\n")

height = len(board1)
width = len(board1[0])

def move_up(x, y):
  if x == 0:
    return (0, -1, -1) # Leaves the board
  if board1[x-1][y] == obstacle:
    board1[x][y] = walked_ALL
    return (">", x, y) # Turn right
  next = board1[x-1][y]
  if next == walked_LR:
    board1[x-1][y] = walked_ALL
  else:
    board1[x-1][y] = walked_UD
  return ("^", x-1, y) # Move up

def move_right(x, y):
  if y == width-1:
    return (0, -1, -1) # Leaves the board
  if board1[x][y+1] == obstacle:
    board1[x][y] = walked_ALL
    return ("v", x, y) # Turn down
  next = board1[x][y+1]
  if next == walked_UD:
    board1[x][y+1] = walked_ALL
  else:
    board1[x][y+1] = walked_LR
  return (">", x, y+1) # Move right

def move_down(x, y):
  if x == height-1:
    return (0, -1, -1) # Leaves the board
  next = board1[x+1][y]
  if next == obstacle:
    board1[x][y] = walked_ALL
    return ("<", x, y) # Turn left
  if next == walked_LR:
    board1[x+1][y] = walked_ALL
  else:
    board1[x+1][y] = walked_UD
  return ("v", x+1, y) # Move down

def move_left(x, y):
  if y == 0:
    return (0, -1, -1) # Leaves the board
  next = board1[x][y-1]
  if next == obstacle:
    board1[x][y] = walked_ALL
    return ("^", x, y) # Turn up
  if next == walked_UD:
    board1[x][y-1] = walked_ALL
  else:
    board1[x][y-1] = walked_LR
  return ("<", x, y-1) # Move left

def move_guard(guard):
  v, x, y = guard
  moves = {"^": move_up, ">": move_right, "v": move_down, "<": move_left}
  return moves[v](x, y)

def walk_until_out_of_board(guard):
  while True:
    guard = move_guard(guard)
    print_board(board1)
    time.sleep(0.1)
    if guard[0] == 0: return

walk_until_out_of_board(guard)

if is_example: print_board(board1)
print(sum([i.count(walked_UD) + i.count(walked_LR) + i.count(walked_ALL) for i in board1]))
