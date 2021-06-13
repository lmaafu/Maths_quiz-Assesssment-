import random 

# Function go here
def choice_checker(question):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "+" or response == "addition":
            return response
        elif response == "-" or response == "subtraction":
            return response

        elif response == "*" or response == "multiplication":
            return response
          
        elif response == "/" or response == "division":
            return response

# check foe exit code
        elif response == "xxx":
            return response
        else:
            print()

# Main routine goes here

error = " !!!Please enter an whole number between 1 and 20!!! "

rounds_played = 0 
rounds = choice_checker 

valid = False
while not valid:
    try:
        #   ask the question
        print()
        response = int(input(" How many questions would you like ? "))

        # if the amount is too low ? too high give
        if 0 < response <= 20:
            print( " You have asked for {} questions " . format(response))


        # output an error
        else:
            print()
            print(error)

    except ValueError:
            print()  
            print(error)

# Rounds Heading 
  # Continious Mode 
if rounds == "":
    heading = "Continuous Mode: Question {}".format(rounds_played + 1)
    print(heading)
    choose = input ("{} or'xxx' to end: ".format(choice_checker))

    print()
    heading = "Question {}".format(rounds_played + 1)
    print(heading)
    choose = input()
    if rounds_played == rounds + 1:

      rounds_played += 1


      chosen_number = random.randint(1,20)
      choose_number = random.randint(1,20)


      question = "{}  {}".format(chosen_number,choose_number)
      answer = eval(question)

    print(question)
    print(answer)



