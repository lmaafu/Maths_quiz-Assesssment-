# Functions go here


# Main routine goes here

error = " !!!Please enter an whole number between 1 and 20!!! "

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

