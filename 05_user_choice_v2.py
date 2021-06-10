# Version 3- checks that response in a given list

# Function go here 
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

  # iterstes through list and if resonse is an item
  # in the list (or the first leter of an item), the 
  # full item name is returned

  for item in valid_list:
      if response == item[0] or response == item:
          return item

  # output error if item not in list 
  print(error)
  print()

# Main routuine goes here 


# list for checking responses 
maths_list = ["addition", "multiplication", "subtraction", "division", "xxx"]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

  # Ask user for choice and check it's valid 
  user_choice = choice_checker("Choose addition / division / subtraction /multiplication (+, / , -, *): ", maths_list, "Please choose from addition / division / subtraction /multiplication (or xxx to quit)")

  #print out choice for comparison purposes 
  print()
  print("You choose {}".format(user_choice ))
  print()
