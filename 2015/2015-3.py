from aocd import get_data

input = get_data(day=3, year=2015)


print("\n## Part 1 ##")

houses = {(0,0)}
current = (0,0)

def move(position, direction):
    if direction == '^':
        return (position[0], position[1]+1)
    elif direction == 'v':
        return (position[0], position[1]-1)
    elif direction == '>':
        return (position[0]+1, position[1])
    elif direction == '<':
        return (position[0]-1, position[1])

for direction in input:
    current = move(current, direction)
    houses.add(current)

print(len(houses))


print("\n## Part 2 ##")

houses = {(0,0)}
current_santa = (0,0)
current_robot = (0,0)

for i, direction in enumerate(input):
    if i % 2 == 0 :
        current_santa = move(current_santa, direction)
        houses.add(current_santa)
    else:
        current_robot = move(current_robot, direction)
        houses.add(current_robot)

print(len(houses))
