import random

r = 0
while True:
  r += 1
  print("==================================================")
  print(" | ♥ heart | ♠ spades | ♣ clubs | ♦ diamonds |")
  print("==================================================")
  print(f"Here is your hand, who win? Round: {r}")
  cards_num = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']

  cards_hearts = [(sym + ' ' + '♥') for sym in cards_num]
  cards_spades = [(sym + ' ' + '♠') for sym in cards_num]
  cards_clubs = [(sym + ' ' + '♣') for sym in cards_num]
  cards_diamonds = [(sym + ' ' + '♦') for sym in cards_num]

  cards = cards_diamonds + cards_hearts + cards_spades + cards_clubs

  # mix cards
  random.shuffle(cards)

  user_cards = cards[:5]
  cpu_cards = cards[5:10]
  
  print("**************************************************")    
  print(f"* Your cards: {user_cards}")
  print("**************************************************")
  print(f"* CPU cards : {cpu_cards}")
  print("**************************************************")
  finish = input("Want to finish?\
     Press F \n Press Enter to continue: ")
  if finish.upper() == "F":
    break

