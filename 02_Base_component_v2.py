
import random

# Functions goes here 
# This gives the user valid responses and also has an error statement if the user doesnt use it correctly 
def choice_checker(question, valid_list, error):

  valid = False
  while not valid: 
    # Ask user for choice (and put choice in lower case)
    response = input(question).lower()

    # iterstes through list and if resonse is an item
    # in the list (or the first leter of an item), the 
    # full item name is returned

    for item in valid_list:
        if response == item[0] or response == item:
            return item

    # output error if item not in list 
    print(error)
    print()


# Instructions for the user 
def instructions ():
    print()
    print(" **** Instructions  **** ")
    print()
    print(" In this quiz we would first ask you which maths operation you would like the use. ")
    print()
    print("Here are your choices :-")
    print("-Addition (+)")
    print("-Subtraction (-)")
    print("-Multiplication (*)")
    print("-Division (/)")
    print()
    print("Then the game will ask for the number of questions you would like ") 
    print("The Game will then give various questions depending on the amount of questions you want and  which maths operation you would like to use ")
    print()
    print("If you want to end the game say 'xxx' and the game will end ")
    print()
    print("After each of your asnwers the game will let you know if you had either a correct answer or wrong answer ")
    print()
    print("At the end of the game it will show you  your results")
    print()
    print("This game will help test out your knowledge if not then improve it ")
    print()
    print(" GOOD LUCK ")

    return""

# This decorates the sides and top of headings 
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Checkes that the user has valid answers for each question 
def int_check(question, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        response = input(question).lower()

        if exit_code == "xxx" and response == "xxx":
            return response
        elif exit_code == "" and response == "":
            return response

        situation = ""

        if low is not None and high is not None:
            situation = "both"
        elif low is not None and high is None:
            situation = "low only "

        try:
            response = int(response)

            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(
                        low, high))
                    continue

            # checks input is not too low
            elif situation == "low only ":
                if response < low:
                    print(
                        "Plese enter a number that is more than (or equal to) {}"
                        .format(low))
                    continue

            return response

        # Checks iput is integer
        except ValueError:
            print("Please enter an integer")
            continue

# Main routine ...

# list of valid responses 
maths_list = ["addition", "+", "multiplication", "*", "subtraction", "-",  "division", "/",  "xxx"]
yes_no_list = ["yes", "no"]
# If the user wants to see instrutions for the game 
played_before = choice_checker("Would like to display instructions? " , yes_no_list, "!!!!PLEASE ANSWER YES OR NO!!!!")

if played_before == "yes":
  instructions()
  print()


# Ask user choice and check it's valid
user_choice = choice_checker("Choose addition / division / subtraction /multiplication (+, / , -, *): ", maths_list, "Please choose from addition / division / subtraction /multiplication (or xxx to quit)")

# choices for the user 
if user_choice == "+" or user_choice == "addition":
  user_choice = "+"
elif user_choice == "-" or user_choice == "subtraction":
  user_choice = "-"
elif user_choice == "*" or user_choice == "multiplication":
  user_choice = "*"
elif user_choice == "/" or user_choice == "division":
  user_choice = "/"

# Game History
game_summary = [] 

# asking for the number of questios 
rounds = int_check("How many questions would you like  : ", 0, exit_code="") 
 
# Rounds
rounds_lost = 0
rounds_won = 0
rounds_played = 0

# Ask user for # of rounds, <enter> for infinite mode 
feedback = ""

keep_going = "yes"

while keep_going == "yes":

  if keep_going == "no":
    break

  else:
    if rounds == rounds_played:
      break
  
  print()
  # Continious Mode 
  if rounds == "":
    heading = "Continuous Mode: Question {}".format(rounds_played + 1)
    # puts stars above / below heading to make it stand out
    heading_decoration = "*"
    statement_generator(heading, heading_decoration)
    
    rounds_played += 1
  else:
    print()
    # Number of rounds 
    heading = "Question {}".format(rounds_played + 1)
    if rounds_played == rounds + 1:
      end_game ="yes"
    # puts lines above / below heading to make it stand out
    heading_decoration = "|"
    statement_generator(heading, heading_decoration)

    rounds_played += 1

  # Compare choices
  
  # If user choose multiplication 
  if user_choice == "*":
    num_1 = random.randint(1,12)
    num_2 = random.randint(1,12)
   # If user choose division  
  if user_choice == "/":
    num_2 = random.randint(1,12) 
    num_3 = random.randint(1,12)
    num_1 = num_2 * num_3  
  # If user choose addition and subtrction  
  if user_choice == "+" or user_choice =="-": 
    num_1 = random.randint(1,30)
    num_2 = random.randint(1,30)
  # generating the question
  print("What is... ")
  question = "{} {} {}  ".format( num_1, user_choice, num_2  )
  print(question)
  # user's answer 
  result  = int_check("Answer: ", exit_code="xxx") 

  # the actual answer for each question
  answer  = eval(question)

  # If exit_code is typed in this should break the loop
  if result == "xxx": 
    keep_going = "no"
    break 
  # Checks if the answer that the user  gave was either correct or incorrect 
  if result != answer:
      feedback = "INCORRECT (The correct answer was {})".format(answer)
      rounds_lost += 1
      print(feedback)
  
  elif result == answer:
      feedback = "CORRECT" 
      print("Well done you got it!")
      rounds_won += 1
      print(feedback)

  # End Game statement_generator
  round_result = "Question {} = ( {}= {} ): {}  ".format(rounds_played, question, result,  feedback)
  game_summary.append(round_result)

# Overall results 
print()
print("CORRECT: {}, INCORRECT: {}".format(rounds_won, rounds_lost,))


#  **** Calculate Game Stats *****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

# Game History
print()
print("***** Game History *******")
for game in game_summary:
  print(game)
  print()

# display game stats with % values to the nearest whole number
print("***** Game Statistics *******")
print("Correct: {} ({:.0f}%)\nIncorrect: {} ({:.0f}%)\n ".format(rounds_won, percent_win, rounds_lost, percent_lose, ))

print("Hope you enjoyed")