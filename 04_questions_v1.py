def int_check(question, low=None, high=None): 

  situation = ""

  if low is not None and high is not None: 
    situation = "both"
  elif low is not None and high is None:
    situation = "low only "

  while True:

    try:
        response = int(input(question))

        # checks input is not too high or
        # too low if a both upper and lower bounds 
        # are specified 
        if situation == "both":
          if response < low or response > high:
            print("Please enter a number between {} and {}".format(low, high))
            continue

        # checks input is not too low 
        elif situation == "low only ":
          if response < low:
              print("Please enter a number that is more than (or equal to) {}".format(low))
              continue

        return response 

    # Checks iput is integer 
    except ValueError:
      print("Please enter an integer")
      continue


