# Component one - round input checker
# Checks input is greater than low (3)
# Checks input is less than high (20)

# Number checking function for rounds/questions input


def num_check(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                valid = True
                return response
            else:
                print("You did not enter a number between {} and {}".format(low, high))
        except ValueError:
            print("Invalid input")


# Minimum questions (rounds) is 3 instead of 1 so the game doesnt end quickly and gives the user's end results
# (component 7) variety. Max is set to 20 so the game isn't overly long
question = num_check("How many questions would you like to answer? (20 max) >>> ", 3, 20)

print("Round: {}".format(question))
