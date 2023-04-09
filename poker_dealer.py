import random

while True:
  print("<3 heart | => spades | =3 trebol | <> diamonds ")
  print("Here is your hand, who win?")
  cards_num = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']

  cards_hearts = [(sym + ' ' + '<3') for sym in cards_num]
  cards_spades = [(sym + ' ' + '=>') for sym in cards_num]
  cards_trebol = [(sym + ' ' + '=3') for sym in cards_num]
  cards_diamonds = [(sym + ' ' + '<>') for sym in cards_num]

  cards = cards_diamonds + cards_hearts + cards_spades + cards_trebol

  # mix cards
  random.shuffle(cards)

  user_cards = cards[:5]
  cpu_cards = cards[5:10]
      
  print(f"Your cards: {user_cards}")
  print(f"CPU cards: {cpu_cards}")
  finish = input("Want to finish? \
    \nPress F or press Enter to continue: ")
  if finish.upper() == "F":
    break

