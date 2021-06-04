import math
import random

# Functions goes here 
# Choices the user can choose from for ther quiz 
def choice_checker(question, valid_list, error):

  # Ask user for choice (and put choice in lower case)
  response = input(question).lower()

  if response == "+" or response == "addition":
    if response == "+":
      response = "addition"
    return response
  elif response == "-" or response == "subtraction":
    if response == "-":
      response = "subtraction"
    return response

  elif response == "*" or response == "multiplication":
    if response == "*":
      response = "multiplication"
    return response
          
  elif response == "/" or response == "division":
    if response == "/":
      response = "division"
    return response

# check foe exit code
  elif response == "xxx":
            return response
  else:
      print()

  

  # iterstes through list and if resonse is an item
  # in the list (or the first leter of an item), the 
  # full item name is returned

  for item in valid_list:
      if response == item[0] or response == item:
          return item

  # output error if item not in list 
  print(error)
  print()

# This checks if the user answered the question with yes or no 
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("!!!!PLEASE ANSWER YES OR NO!!!!")
            print()

# Instructions for the user 
def instructions ():
    print()
    print(" **** Instructions  **** ")
    print()
    print(" rules go here ")
    print()
    return""

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# integer Checker 
def int_check(question, low=None, high=None): 

  situation = ""

  if low is not None and high is not None: 
    situation = "both"
  elif low is not None and high is None:
    situation = "low only "

  while True:

    try:
        response = int(input(question))

        # checks input is not too high or
        # too low if a both upper and lower bounds 
        # are specified 
        if situation == "both":
          if response < low or response > high:
            print("Please enter a number between {} and {}".format(low, high))
            continue

        # checks input is not too low 
        elif situation == "low only ":
          if response < low:
              print("Please enter a number that is more than (or equal to) {}".format(low))
              continue

        return response 

    # Checks iput is integer 
    except ValueError:
      print("Please enter an integer")
      continue

      
# Main routine .....
# list for checking responses 
maths_list = ["addition", "multiplication", "subtraction", "division", "xxx"]

# If the user wants to see instrutions of hoe tyo play the game 
played_before= yes_no("Would like to display instructions? ")

if played_before == "yes":
    instructions()
print()
print("Programe continues")

# Set up the gam parameters (range, number of numbers)
low = int(input("Low Number: "))
print()
high = int(input(" High Number: "))
print()
rounds = int(input(" Rounds: "))

# works out nmber of guesses 
num_range = high - low + 1
max_raw = math.log2(num_range)  # finds maximum # of guesses using math.log2
max_upped = math.ceil(max_raw)  # rounds up (ceil----> ceiling )
max_guesses = max_upped + 1

print("Max Guesses: {}".format(max_guesses ))
print()
# Rounds

rounds_lost = 0
rounds_won = 0  
rounds_played = rounds_won + rounds_lost 
# Rounds Heading 
rounds_played = 0
choose_instructions = "Please choosed addition(+), subtraction(-), multiplication(*), or division(/) : "

# Ask user for # of rounds, <enter> for infiniye mode 
rounds = int_check()

end_game = "no"
while end_game == "no":

    # Rounds Heading 
    print()
    if rounds == "":
      heading = "Continuous Mode: Round {}".format(rounds_played + 1)
      print(heading)
      choose = input ("{} or'xxx' to end: ".format(choose_instructions))
      if choose == "xxx":
            break
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        choose = input(choose_instructions)
        if rounds_played == rounds + 1:
          end_game ="yes"

        rounds_played += 1


    # rest of loop / game
    if choose == "+":
      choose = "addition"
    if choose == "-":
      choose = "subtraction"
    if choose == "*":
      choose = "multiplication"
    if choose == "/":
      choose = "division"
print("You chose {}".format(choose))



print("Thank you for playing")
