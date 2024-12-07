from aocd import get_data
import itertools

is_example = False

if not is_example: input = get_data(day=7, year=2024).strip().split("\n")
else: input = open("2024/7.in").read().strip().split("\n")

input = [i.split(":") for i in input]
input = {int(i[0]): [int(j) for j in i[1].split()] for i in input}

print("\n## Part 1 ##\n")

def add(a, b): return a + b
def mul(a, b): return a * b

def concat(a, b): return int(str(a) + str(b))

def is_possible(result, operands, ops):
  for prod in itertools.product(ops, repeat=len(operands) - 1):
    acc = operands[0]
    e = str(acc)
    for i in range(1, len(operands)):
        next_op = prod[i - 1]
        if next_op == add: e += "+"
        elif next_op == mul: e += "*"
        elif next_op == concat: e += "||"
        
        acc = next_op(acc, operands[i])
        e += str(operands[i])
        
        if acc > result: break
    if acc == result: return e
  return "x"

def solve(ops):
  sum = 0
  for i in input:
    a = is_possible(i, input[i], ops)
    if a != "x":
      sum += i
      print(str(i).rjust(15), f"\033[92m{a}\033[0m")
    else: print(str(i).rjust(15), f"\033[91m{a}\033[0m")
  print(sum)

solve([add, mul])

print("\n## Part 2 ##\n")

solve([add, concat, mul])
