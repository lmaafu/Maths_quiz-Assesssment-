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

def check_rounds():
  while True: 
    print()
    response = input("How many rounds?: ")

    rounds_error = "Please type either <enter> or an integer that is more than 0"
    if response != "":
      try:
        response = int(response)

        if response <1:
          print(rounds_error)
          continue 

        else:
          return response

      except ValueError:
        print(rounds_error)
        continue

    return response 

# Main routine goes here .....


rounds_played = 0
choose_instructions = "Please choosed addition(+), subtraction(-), multiplication(*), or division(/)"

# Ask user for # of rounds, <enter> for infiniye mode 
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading 
    print()
    if rounds == "":
      heading = "Continuous Mode: Round {}".format(rounds_played)
      print(heading)
      choose = input ("{} or'xxx' to end: ".format(choose_instructions))
      if choose == "xxx":
            break
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
    print(heading)
    choose = input(choose_instructions)
    if rounds_played == rounds - 1:
      end_game ="yes"


    # rest of loop / game
print("You chose {}".format(choose))

rounds_played += 1

print("Thank you for playing")
