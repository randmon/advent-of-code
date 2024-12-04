from aocd import get_data

# input = get_data(day=7, year=2023).strip().split("\n")
input = open("test.txt").read().strip().split("\n")

print("\n## Part 1 ##")

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def get_index(card):
  return cards.index(card[0])

def is_better(card1, card2):
  return get_index(card1) > get_index(card2)

def is_five_of_a_kind(hand):
  return 5 in hand.values()

def is_four_of_a_kind(hand):
  return 4 in hand.values()

def is_full_house(hand):
  return 3 in hand.values() and 2 in hand.values()

def is_three_of_a_kind(hand):
  return 3 in hand.values()

def is_two_pairs(hand):
  return list(hand.values()).count(2) == 2

def is_one_pair(hand):
  return 2 in hand.values()

def calculate_cards_by_combi(hand):
  if is_five_of_a_kind(hand):
    return 7
  if is_four_of_a_kind(hand):
    return 6
  if is_full_house(hand):
    return 5
  if is_three_of_a_kind(hand):
    return 4
  if is_two_pairs(hand):
    return 3
  if is_one_pair(hand):
    return 2
  return 1

def calculate_cards_by_value(hand, n_cards_in_hand):
  h = list(reversed(hand))
  print(h)
  result = 0
  for i, card in enumerate(h):
    result += get_index(card) * (n_cards_in_hand ** i)
  return result
  
  
hands = [h.split() for h in input]
n_cards_in_hand = len(list(hands[0][0]))
print("cards in hand:", n_cards_in_hand, "\n")

for hand in hands:
  play = list(hand[0])
  
  mapped = { card: play.count(card) for card in play }
  print(hand[0], ":", mapped)
  combi = calculate_cards_by_combi(mapped) * ((10 ** (n_cards_in_hand*2))) + calculate_cards_by_value(play, n_cards_in_hand)
  print(calculate_cards_by_value(play, n_cards_in_hand))
  print("----\n")