from aocd import get_data

input = get_data(day=4, year=2023).strip().split("\n")
# input = open("test.txt").read().strip().split("\n")

cards = [[x.split() for x in line.split(":")[1].strip().split(" | ")] for line in input]


print("\n## Part 1 ##")

total = 0

def get_matches(card):
    return len(set(card[0]).intersection(card[1]))
  
for card in cards:
    matches = get_matches(card)
    if matches > 0:
        total += 2 ** (matches-1)
    
print(total)


print("\n## Part 2 ##")

cards_in_hand = {}

for i, card in enumerate(cards):
    if i not in cards_in_hand:
        cards_in_hand[i] = 1
    
    matches = get_matches(card)
    
    for next_card in range(i+1, i+1+matches):
        cards_in_hand[next_card] = cards_in_hand.get(next_card, 1) + cards_in_hand[i]
        
print(sum(cards_in_hand.values()))
    