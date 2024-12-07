from aocd import get_data
from utils import bcolors

is_example = False

if is_example: input = open("2023/7.in").read().strip().split("\n")
else: input = get_data(day=7, year=2023).strip().split("\n")

print(f"\n{bcolors.CLEAR}## Part 1 ##")

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
    if is_example: print(f"{bcolors.HEADER}Five of a kind{bcolors.ENDC}")
    return 7
  elif is_four_of_a_kind(hand):
    if is_example: print(f"{bcolors.OKBLUE}Four of a kind{bcolors.ENDC}")
    return 6
  elif is_full_house(hand):
    if is_example: print(f"{bcolors.OKCYAN}Full house{bcolors.ENDC}")
    return 5
  elif is_three_of_a_kind(hand):
    if is_example: print(f"{bcolors.OKGREEN}Three of a kind{bcolors.ENDC}")
    return 4
  elif is_two_pairs(hand):
    if is_example: print(f"{bcolors.WARNING}Two pairs{bcolors.ENDC}")
    return 3
  elif is_one_pair(hand):
    if is_example: print(f"{bcolors.FAIL}One pair{bcolors.ENDC}")
    return 2
  else:
    if is_example: print(f"High card")
    return 1

def calculate_cards_by_value(hand):
  h = list(reversed(hand))
  if is_example: print(h)
  result = 0
  for i, card in enumerate(h):
    value = get_index(card)
    add = value * (100 ** (i))
    result += add
    
    if is_example: print(f"{card} -> {str(value).ljust(2)} * 10^{i} = {str(add).rjust(10)}")
    
  return result
  
  
hands = [h.split() for h in input]
n_cards_in_hand = len(list(hands[0][0]))
if is_example: print("cards in hand:", n_cards_in_hand, "\n")

hands_with_values = {
  "hand": [],
  "value": [],
  "bet": 0
}

unsorted_hands = []

for hand in hands:
  play = list(hand[0])
  if is_example: print(" ".join(play))
  
  mapped = { card: play.count(card) for card in play }
  combi = calculate_cards_by_combi(mapped)
  combi = int(str(combi).ljust(n_cards_in_hand*2+1, "0"))
  value = calculate_cards_by_value(play)
  
  total = combi + value
  if is_example: print(f"Total: {total}")
  
  unsorted_hands.append(hands_with_values.copy())
  unsorted_hands[-1]["hand"] = play
  unsorted_hands[-1]["value"] = total
  unsorted_hands[-1]["bet"] = int(hand[1])
  
  if is_example: print("----\n")
  
sorted_hands = sorted(unsorted_hands, key=lambda x: x["value"])

total_bets = 0

for i in range(len(sorted_hands)):
  hand = sorted_hands[i]
  this_bet = hand["bet"]*(i+1)
  if is_example: print(f"{bcolors.BOLD}{bcolors.OKBLUE}{hand['hand']}{bcolors.ENDC} with {hand['value']} points, bet: {hand['bet']} * {i+1} = {this_bet}")
  total_bets += this_bet
  
print("\nTotal bets:", total_bets)