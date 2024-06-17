import random
from typing import List, Tuple


SUITS = "♠ ♡ ♢ ♣".split()

RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

Card = Tuple[str, str]
Deck = List[Card]

def create_deck(shuffle: bool = False) -> Deck:
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items):
    return random.choice(items)

def player_order(names, start=None):
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]
  
def card_value(card):
  suit, rank = card
  value = 0
  if rank.isdigit():
    value = int(rank)
  elif rank in "JQK":
    value = 10
  elif rank == "A":
    value = 11
  if suit in "♠♣":
    value *= 2
  return value

def play(seed_value):
  random.seed(seed_value)
  deck = create_deck(shuffle=True)
  names = "P1 P2 P3 P4".split()
  hands = {n: h for n, h in zip(names, deal_hands(deck))}
  start_player = choose(names)
  turn_order = player_order(names, start=start_player)

  points = {name: 0 for name in names}
  while hands[start_player]:
    turn_winners = []
    max_value = 0
    for name in turn_order:
      card = choose(hands[name])
      hands[name].remove(card)
      value = card_value(card)
      if value > max_value:
        turn_winners = [name]
        max_value = value
      elif value == max_value:
        turn_winners.append(name)
    for winner in turn_winners:
      points[winner] += 1

  winners = [name for name, point in points.items() if point == max(points.values())]
  return " ".join(sorted(winners))