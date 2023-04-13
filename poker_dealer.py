import random

r = 0
win_cpu = 0
win_user = 0
while True:
  r += 1
  print("==================================================")
  print(" | ♥ heart | ♠ spades | ♣ clubs | ♦ diamonds |")
  print("==================================================")
  # print(f"Here are your cards\nWho win, USER or CPU? Round: {r}")
  print("Here are your cards")
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
  print(f"* USER cards: {user_cards}")
  print("**************************************************")
  print(f"* CPU cards : {cpu_cards}")
  print("**************************************************")
  print("Who win, USER (u) or CPU (c)?")
  win = input("The winner is ").lower()
  if win == "u":
    win_user += 1
  elif win == "c":
    win_cpu += 1
  else:
    pass
  print("**************************************************")
  print(f"Win CPU: {win_cpu} | Win USER: {win_user} | Round: {r}")
  print("**************************************************")
  finish = input("Want to finish?\
     Press F \n Press Enter to continue: ")
  if finish.upper() == "F":
    break

