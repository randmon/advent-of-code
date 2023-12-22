from aocd import get_data

input = get_data(day=1, year=2022).strip().split("\n\n")

input = [i.split("\n") for i in input]
input = [[int(j) for j in i] for i in input]


print("\n## Part 1 ##")

result = max([sum(i) for i in input])

print(result)


print("\n## Part 2 ##")

top3 = sorted([sum(i) for i in input], reverse=True)[:3]

print(sum(top3))