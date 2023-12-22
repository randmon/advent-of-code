from aocd import get_data

input = get_data(day=2, year=2022).strip().split("\n")

print("\n## Part 1 ##")

points_play = {"A": 1, "B": 2, "C": 3}
points_win = {"X": 6, "Y": 3, "Z": 0}

def calculate_points(opponent, me):
    if opponent == me:
        return points_play[me] + 3
    elif (opponent == "A" and me == "B") or (opponent == "B" and me == "C") or (opponent == "C" and me == "A"):
        return points_play[me] + 6
    elif (opponent == "A" and me == "C") or (opponent == "B" and me == "A") or (opponent == "C" and me == "B"):
        return points_play[me]
    else:
        raise ValueError("Invalid input")

strategy1 = [x.replace("X", "A").replace("Y", "B").replace("Z", "C") for x in input]
result = sum([calculate_points(line[0], line[2]) for line in strategy1])

print(result)


print("\n## Part 2 ##")

def make_move(opponent, result):
    if result == "X":
        return {"A": "B", "B": "C", "C": "A"}[opponent]
    elif result == "Y":
        return opponent
    elif result == "Z":
        return {"A": "C", "B": "A", "C": "B"}[opponent]
    else:
        raise ValueError("Invalid input")

total = 0
for line in input:
    opponent = line[0]
    result = line[2]
    me = make_move(opponent, result)
    total += points_win[result] + points_play[me]
    
# TODO: This is not correct
print(total) 