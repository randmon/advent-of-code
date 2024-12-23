from aocd import get_data
import time
from utils import bcolors

is_example = False
if is_example: input = open("2024/6.in").read().strip().split("\n")
else: input = get_data(day=6, year=2024).strip().split("\n")

UP = "^"
RIGHT = ">"
DOWN = "v"
LEFT = "<"

print("\033c\n## Part 2 ##")

def print_board(board, count):
  output = "\033c\n## Part 2 ##\n\n"
  
  for i in board:
    for j in i:
      if j["UP"]:
        output += f"{bcolors.BLUE}{bcolors.BOLD}^{bcolors.ENDC} "
      elif j["RIGHT"]:
        output += f"{bcolors.BLUE}{bcolors.BOLD}>{bcolors.ENDC} "
      elif j["DOWN"]:
        output += f"{bcolors.BLUE}{bcolors.BOLD}v{bcolors.ENDC} "
      elif j["LEFT"]:
        output += f"{bcolors.BLUE}{bcolors.BOLD}<{bcolors.ENDC} "
      elif j["obstacle"]:
        output += f"{bcolors.RED}{bcolors.BOLD}#{bcolors.ENDC} "
      elif j["new_obstacle"]:
        output += f"{bcolors.CYAN}{bcolors.BOLD}O{bcolors.ENDC} "
      else:
        output += f"{bcolors.YELLOW}{bcolors.BOLD}.{bcolors.ENDC} "
    output += "\n"
  output += f"\nCount: {count}\n"
  print(output)

def find_guard(input):
  for i in range(len(input)):
    for j in range(len(input[i])):
      if input[i][j] in ["^", ">", "v", "<"]:
        return (input[i][j], i, j)

cell = {
  "UP": False,
  "RIGHT": False,
  "DOWN": False,
  "LEFT": False,
  "obstacle": False,
  "new_obstacle": False
}

def init_board(input):
  new_board = []
  for i in input:
    row = []
    for j in i:
      cell = {
        "UP": False,
        "RIGHT": False,
        "DOWN": False,
        "LEFT": False,
        "obstacle": False,
        "new_obstacle": False
      }
      if j == "#":
        cell["obstacle"] = True
      elif j == "^":
        cell["UP"] = True
      elif j == ">":
        cell["RIGHT"] = True
      elif j == "v":
        cell["DOWN"] = True
      elif j == "<":
        cell["LEFT"] = True
      row.append(cell)
    new_board.append(row)
  return new_board
  
guard_start_pos = find_guard(input)
board = init_board(input)

height = len(board)
width = len(board[0])

def move_up(x, y, board):
  board[x][y]["UP"] = True
  if x == 0: return ((0, -1, -1), board) # Leaves the board
  next = board[x-1][y]
  if next["obstacle"] or next["new_obstacle"]: return ((RIGHT, x, y), board) # Turn right
  if next["UP"]: return ((-1, -1, -1), board) # Enters a loop
  return ((UP, x-1, y), board)

def move_right(x, y, board):
  board[x][y]["RIGHT"] = True
  if y == width-1: return ((0, -1, -1), board) # Leaves the board
  next = board[x][y+1]
  if next["obstacle"] or next["new_obstacle"]: return ((DOWN, x, y), board) # Turn down
  if next["RIGHT"]: return ((-1, -1, -1), board) # Enters a loop
  return ((RIGHT, x, y+1), board)

def move_down(x, y, board):
  board[x][y]["DOWN"] = True
  if x == height-1: return ((0, -1, -1), board) # Leaves the board
  next = board[x+1][y]
  if next["obstacle"] or next["new_obstacle"]: return ((LEFT, x, y), board) # Turn left
  if next["DOWN"]: return ((-1, -1, -1), board) # Enters a loop
  return ((DOWN, x+1, y), board)

def move_left(x, y, board):
  board[x][y]["LEFT"] = True
  if y == 0: return ((0, -1, -1), board) # Leaves the board
  next = board[x][y-1]
  if next["obstacle"] or next["new_obstacle"]: return ((UP, x, y), board) # Turn up
  if next["LEFT"]: return ((-1, -1, -1), board) # Enters a loop
  return ((LEFT, x, y-1), board)

moves = {"^": move_up, ">": move_right, "v": move_down, "<": move_left}

def move_guard(guard, board):
  v, x, y = guard
  return moves[v](x, y, board)

def goes_out_of_board(guard, board):
  while True:
    (guard, board) = move_guard(guard, board)
    if is_example:
      print_board(board, count)
      time.sleep(0.1)
    if guard[0] == 0: return True
    if guard[0] == -1: return False

def copy_board(board):
  result = []
  for i in board:
    row = []
    for j in i:
      cell = {
        "UP": j["UP"],
        "RIGHT": j["RIGHT"],
        "DOWN": j["DOWN"],
        "LEFT": j["LEFT"],
        "obstacle": j["obstacle"],
        "new_obstacle": j["new_obstacle"]
      }
      row.append(cell)
    result.append(row)
  return result

def add_obstacle(x, y, board):
  new_board = copy_board(board)
  new_board[x][y]["new_obstacle"] = True
  return new_board

count = 0
height = len(board)
width = len(board[0])

def guard_positions_without_new_obstacles(board):
  positions = []
  guard = guard_start_pos
  while True:
    (guard, board) = move_guard(guard, board)
    if guard[0] == 0: return positions
    if guard[0] == -1: raise Exception("Guard entered a loop in initial board")
    if not guard_already_in_positions(guard, positions):
      positions.append(guard)

def guard_already_in_positions(guard, positions):
  if (guard[1], guard[2]) == (guard_start_pos[1], guard_start_pos[2]): return True
  for pos in positions:
    if (guard[1], guard[2]) == (pos[1], pos[2]):
      return True
  return False

successful_obstacles = []
for pos in guard_positions_without_new_obstacles(copy_board(board)):
  guard = guard_start_pos
  new_board = add_obstacle(pos[1], pos[2], board)
  if not goes_out_of_board((guard[0], guard[1], guard[2]), new_board):
    count += 1
    successful_obstacles.append(pos)
    if not is_example: print(f"{count} - {pos[1], pos[2]}")

