# Component four, random numbers generated into a statement and new set of numbers appear with each round

import random


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
# function that allows float numbers (decimal point)


def qst_statement(question):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print("Invalid input, try again")


keep_going = ""
while keep_going == "":

    # How many rounds user is going to play, range between 1 and 20
    # So user doesn't make a game too long
    # So doesn't break the game due to entering 0 or a negative number as the game will instantly end

    rounds = num_check("How many questions would you like to answer? (max 20) >>> ", 3, 20)
    print()

    # Sets counters to 0
    round_counter = 0

    # Waits for the number of rounds played reach number of rounds needed to play then stop the game
    while round_counter < rounds:

        # Generates and prints the numbers at the the start of each round. (prints for testing purposes)
        a = round(random.uniform(1, 100), 2)
        print("#1 = {}".format(a))
        b = round(random.uniform(1, 100), 2)
        print("#2 = {}".format(b))

        # Sum of the preceding random numbers
        total = round(a + b, 2)
        print("Total = {:.2f}\n".format(total))

        # Adds a +1 round counter at the start of each round
        round_counter += 1

        # Prints the current round that the user is on
        print("Round ({})\n".format(round_counter))

        # Asks question
        answer = qst_statement("What does {} + {} = ".format(a, b))

        # Checks if the answer is correct to the preceding question
        if answer == total:
            # Win statement
            print("correct\n")
        else:
            # Lose statement
            print("Incorrect, the answer was {}\n".format(total))

    # Loop of function
    keep_going = input("Press <enter> to play again or any key to stop. >>> ")
