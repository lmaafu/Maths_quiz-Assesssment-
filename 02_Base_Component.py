
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
    print(" In this quiz we would first ask you which maths operation you would like the use. ")
    print()
    print("Here are your choices :-")
    print("-Addition")
    print("-Subtraction")
    print("-Multiplication")
    print("-Division")
    print()
    print("Then the game will ask for the number of questions you would like ") 
    print("The Game will then give various questions depending on the amount of questions you want and the which maths operation you would like to use ")
    print()
    print("PLEASE KNOW THAT THE NUMBERS THAT ARE GIVEN ARE RANDOM AND IS FROM A RANGE OF NUMBERS FROM 1 - 20 ")
    print()
    print("If you want to end the game say 'xxx' and the game will end ")
    print()
    print("After each of your asnwers the game will let you know if you had either a correct answer or wrong answer ")
    print()
    print("At the end of the game it will show you  your results")
    print()
    print("This game will help test out your knowledge if not then improve it ")
    print()
    print("GOOD LUCK!!!")





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

      
# Main routine .....
rounds_played = 0
# list for checking responses 
maths_list = ["addition", "multiplication", "subtraction", "division", "xxx"]
# Ask user choice and check it's valid
user_choice = choice_checker("Choose addition / division / subtraction /multiplication (+, / , -, *): ", maths_list, "Please choose from addition / division / subtraction /multiplication (or xxx to quit)")
print()

# If the user wants to see instrutions of hoe tyo play the game 
played_before = yes_no("Would like to display instructions? ")

if played_before == "yes":
    instructions()
print()
# Game History
game_summary = [] 
# list
scores =[]

rounds = int_check(" How many questions would you like  : ", 0, exit_code="") # 

rounds_lost = 0
rounds_won = 0  
rounds_played = rounds_won + rounds_lost 
# Rounds Heading 
rounds_played = 0


# Ask user for # of rounds, <enter> for infiniye mode 
feedback = ""

end_game = "yes"

while end_game == "yes":

  if end_game == "no":
    break

  else:
    if rounds == rounds_played:
      break

  # Rounds Heading 
  print()
  if rounds == "":
    heading = "Continuous Mode: Question {}".format(rounds_played + 1)
    print(heading)
    choose = input ("{} or'xxx' to end: ".format(choice_checker))
    if choose == "xxx":
          break
  else:
    print()
    heading = "Question {}".format(rounds_played + 1)
    print(heading)
    choose = input()
    if rounds_played == rounds + 1:
      end_game ="yes"

    rounds_played += 1

    # Questions for each maths operation and round 
    num_1 = random.randint(1,20)
    num_2 = random.randint(1,20)

    print (num_1, user_choice, num_2)
              


  # End game if exit code is typed 
  if choose == "xxx":
        break 
        
  if rounds == rounds_played: 
    break 

      # Compare choices 




print("Thank you for playing")
