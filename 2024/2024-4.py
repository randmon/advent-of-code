from aocd import get_data
import re

input = get_data(day=3, year=2024)
# with open("3", "w") as f:
#   f.write(input)
  
# input = input.replace("\n", "N")
  
print("\n## Part 1 ##")

pattern = r"mul\((\d+),(\d+)\)"
result = 0
for a, b in re.findall(pattern, input):
  result += int(a) * int(b)

print(result)

print("\n## Part 2 ##")

result = 0

# Remove everything between don't() and do(), and everything after the remaining donts
input = re.sub(r"don't\(\).*?(do\(\))", "*", input)

last_dont = input.find("don't()")
input = input[:last_dont]

for a, b in re.findall(pattern, input):
  result += int(a) * int(b)
  
print(result)