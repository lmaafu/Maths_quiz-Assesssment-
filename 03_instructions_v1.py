# Fuction go here...
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


def instructions ():
    print()
    print(" **** Instructions  **** ")
    print()
    print(" rules go here ")
    print()
    return""

# Main Routine goes here....
played_before= yes_no("Would like to display instructions? ")

if played_before == "yes":
    instructions()
print()
print("Programe continues")