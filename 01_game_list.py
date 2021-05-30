import random 

how_many = 5
won = 0
lost = 0

game_history = []

print()
print("**** World's Lamest Game *** ")
print("Type in 'win'to win, or anything else to lose a round")
print()

for item in range(1, how_many + 1):

  result = input ("Game Result? ")

  if result == "won":
    feedback = "You won"
    won += 1 
  else:
    feedback = "Sorry, you lost"
    lost += 1

  round_result = " Round {} : {} ".format(item, feedback )
  game_history.append(round_result)

print()
print("**** Results ****")

for item in game_history:
  print(item)
