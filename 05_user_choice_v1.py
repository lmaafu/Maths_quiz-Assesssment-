# Version 2 - error message included when calling function


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

# Loop for testing purposes
user_choice = ""
print(choice_checker)
while user_choice != "xxx":

    # Ask user choice and check it's valid
    user_choice = choice_checker(
        "Choose addition / subtraction/ multiplication / divsion  (+, -, *, //): " or "Please choose addition / subtraction/ multiplication / divsion (or xxx to quit)")
        
    # Print ot choice for comparison purposes
    print()
    print("You chose {}".format(user_choice))
    print()
