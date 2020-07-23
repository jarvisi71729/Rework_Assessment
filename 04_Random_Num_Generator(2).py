# Component four (2) - insert random numbers from component four (1) into questions

import random

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

    # To make sure game finishes when user plays all desired rounds
    while round_counter < rounds:

        # Generates two random numbers that will be used in question statement, prints numbers for testing purposes
        a = round(random.uniform(1, 100), 2)
        print("#1 = {}".format(a))
        b = round(random.uniform(1, 100), 2)
        print("#2 = {}".format(b))

        # Total sum of random numbers above (rounded to 2dp), printed for testing purposes
        total = round(a + b, 2)
        print("Total = {:.2f}\n".format(total))

        # Adds one (+1 to counter) round before each question is printed
        round_counter += 1

        # Prints round counter so user can easily keep track
        print("Round ({})\n".format(round_counter))

        # Prints question using randomly generated numbers
        answer = qst_statement("{} + {} = ".format(a, b))

        # Checks if user input is correct (same as total sum of 2 numbers)
        if answer == total:
            # Prints win result if user is correct
            print("Correct\n")
        else:
            # Prints lose result if user is wrong and prints correct answer
            print("Incorrect, the answer was {}\n".format(total))

    # Asks user if they want to play another set of rounds or stop
    keep_going = input("Press <enter> to play again or any key to stop. >>> ")
