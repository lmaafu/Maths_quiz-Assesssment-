# Function used to check input is valid


def check_rounds():
 while True:
   response = input("How many question would you like: ") 

   rounds_error = "Please type either <enter> or an integer that is more than 0"
   if response != "":
      try:
        response = int(response)

        if response < 1:
          print(rounds_error)
          continue 

      except ValueError:
        print(rounds_error)
        continue

      return response 


# Main routine goes here .....


questions_wanted = 0
choose_instructions = "Please choose which mths operstion you would like to test out "

# Ask user for # of rounds, <enter> for infiniye mode 
questions = check_rounds()


end_game = "no"
while end_game == "no":

    # Rounds Heading 
    print()
    if questions == "":
      heading = "Continuous Mode: Round {}".format(questions_wanted)
      print(heading)
      choose = input ("{} or'xxx' to end: ".format(choose_instructions))
      if choose == "xxx":
            break
    else:
        heading = "Round {} of {}".format(questions_wanted + 1, questions)
    print(heading)
    choose = input(choose_instructions)
    if questions_wanted == questions - 1:
      end_game ="yes"


    # rest of loop / game
print("You chose {}".format(choose))

questions_wanted += 1

print("Thank you for playing")

