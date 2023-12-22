from aocd import get_data

input = get_data(day=6, year=2023).strip().split("\n")
# input = open("test.txt").read().strip().split("\n")
# ['Time:        38     94     79     70', 'Distance:   241   1549   1074   1091']

times = [int(x) for x in input[0].split(": ")[1].split()]
distances = [int(x) for x in input[1].split(": ")[1].split()]

races = [(times[i], distances[i]) for i in range(len(times))]

print("\n## Part 1 ##")

print(races)

