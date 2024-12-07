from aocd import get_data
import re

input = get_data(day=4, year=2024).strip().split("\n")
# input = open("test.txt").read().strip().split("\n")

height = len(input)
width = len(input[0])

print("\n## Part 1 ##")

def check(line):
  # Check from left to right and right to left
  return re.findall("XMAS", line) + re.findall("SAMX", line)

def find_xmas(lines):
  return sum([len(check(line)) for line in lines])
  
count = 0 

count += find_xmas(input)

# Turn the board 90 degrees
vertical = ["".join([line[i] for line in input]) for i in range(width)]
count += find_xmas(vertical)

# Search diagonally, top left to bottom right
diagonalLR = []
# Start from the first row, first column and go down to the bottom of the board diagonally
# Then move to the first row, second column, and so on
for col in range(width):
  r = []
  for row in range(height):
    if row+col >= height:
      break
    c = input[row][row+col]
    r.append(c)
  diagonalLR.append("".join(r))

# Now start from the second row, first column and go down to the bottom of the board diagonally
# Then move to the third row, first column, and so on
for row in range(1, height):
  r = []
  for col in range(width):
    if row+col >= width:
      break
    c = input[row+col][col]
    r.append(c)
  diagonalLR.append("".join(r))
  
count += find_xmas(diagonalLR)

# Search diagonally, top right to bottom left
diagonalRL = []

# Start from the first row, last column and go down to the bottom of the board diagonally to the left
# Then move to the first row, second to last column, and so on
for col in range(width-1, 0, -1):
  r = []
  for row in range(height):
    if col-row < 0:
      break
    c = input[row][col-row]
    r.append(c)
  if len(r) >= 4:
    diagonalRL.append("".join(r))
  
# Now start from the second row, last column and go down to the bottom of the board diagonally to the left
# Then move to the third row, last column, and so on
for row in range(1, height):
  r = []
  for col in range(width):
    if row+col >= width:
      break
    actual_col = width - 1 - col
    c = input[row+col][actual_col]
    r.append(c)
  if len(r) >= 4:
    diagonalRL.append("".join(r))
  
count += find_xmas(diagonalRL)

print(count)


print("\n## Part 2 ##")

def find_sam(lines):
  first = lines[0]
  second = lines[1]
  third = lines[2]
  ms = ["M", "S"]
  
  count = 0
  
  for i in range(len(first)-2):
    if second[i+1] == "A":
      if first[i] in ms and first[i+2] in ms:
        if (third[i] in ms and third[i] != first[i+2]) and (third[i+2] in ms and third[i+2] != first[i]):
          count += 1
  return count



result = 0
for i in range(height-2):
  result += find_sam(input[i:i+3])
  
print(result)
