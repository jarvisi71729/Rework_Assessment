# Component five - answer checker
# Component purpose is to add +1 to win counter if correct, adds nothing if user answer is incorrect

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


# Checks user input is a number, allows whole and decimal point numbers


def qst_statement(question):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print("Invalid input, try again")


# Loops entire game
keep_going = ""
while keep_going == "":

    # Minimum questions (rounds) is 3 instead of 1 so the game doesnt end quickly and gives the user's end results
    # (component 7) variety. Max is set to 20 so the game isn't overly long

    rounds = num_check("How many questions would you like to answer? (max 20) >>> ", 3, 20)
    print()

    # Set round counter to zero, 1 round will be added before each question
    round_counter = 0

    # Set win counter to zero, 1 win will be added if user answers correctly
    win_counter = 0

    # To make sure game finishes when user plays all desired rounds
    while round_counter < rounds:

        # Adds one (+1 to counter) round before each question is printed
        round_counter += 1

        # Prints round counter so user can easily keep track
        print("Round ({})\n".format(round_counter))

        # Prints question using set numbers (for testing purposes) - numbers will be replaced with randomly generated
        # numbers with 2 decimal points
        answer = qst_statement("What's 6.01 + 4.23 = ")

        # Checks if user input is correct (same as total sum of 2 numbers)
        if answer == 10.24:
            # Adds +1 to win counter if user input is correct
            win_counter += 1
            # Prints win result if user is correct
            print("Correct\n")
        else:
            # Prints lose result if user is wrong and prints correct answer
            print("Incorrect, the answer was 10.24\n")

        # Prints user game results (how many wins & losses)
        print("WON: {}  |  LOST: {}\n".format(win_counter, round_counter - win_counter))
        # Asks user if they want to play another set of rounds or stop
    keep_going = input("Press <enter> to play again or any key to stop. >>> ")
