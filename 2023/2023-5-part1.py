from aocd import get_data

# input = get_data(day=5, year=2023).strip().split("\n\n")
input = open("test.txt").read().strip().split("\n\n")


print("\n## Part 1 ##")

def convert_input(lines):
    lines = [list(map(int, x.split())) for x in lines.split("\n")[1:]]
    mapping = {}
    for line in lines:
        destination = line[0]
        source = line[1]
        range_length = line[2]-1
        source_range = (source, source + range_length)
        mapping[source_range] = destination - source
    return mapping

mappings = []
for mapping in input[1:]:
    mappings.append(convert_input(mapping))

seeds = [int(x) for x in input[0].split(": ")[1].split()]

def find_in_ranges(ranges_values_map, value):
    for key, val in ranges_values_map.items():
        if key[0] <= value <= key[1]:
            return value + val
    return value

current_numbers = seeds
for mapping in mappings:
    next_numbers = []
    for n in current_numbers:
        next_numbers.append(find_in_ranges(mapping, n))
    current_numbers = next_numbers
    
print(min(current_numbers))