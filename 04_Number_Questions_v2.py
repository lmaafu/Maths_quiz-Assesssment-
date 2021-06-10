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

# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print("*** Round #{} ***".format(rounds_played))
    balance -= 1
    print("Balance: ", balance)
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press enter to pay again or 'xxx' to quit")