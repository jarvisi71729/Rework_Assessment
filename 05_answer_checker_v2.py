# Component five, compares answer to input and adds a +1 win counter if you win round

# Number checker functions

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


# Start of loop
keep_going = ""
while keep_going == "":

    # How many rounds user is going to play, range between 1 and 20
    # So user doesn't make a game too long
    # So doesn't break the game due to entering 0 or a negative number as the game will instantly end

    rounds = num_check("How many questions would you like to answer? (max 20) ", 3, 20)
    print()

    # Sets counters to 0
    round_counter = 0
    win_counter = 0

    # Waits for the number of rounds played reach number of rounds needed to play then stop the game
    while round_counter < rounds:

        # Adds a +1 round counter at the start of each round
        round_counter += 1

        # Prints the current round that the user is on
        print("Round ({})\n".format(round_counter))

        # Generate two random numbers for question

        a = round(random.uniform(1,10),2)
        b = round(random.uniform(1, 10), 2)

        total = round(a+b, 2)

        print(a)
        print(b)
        print(total)
        # Asks question
        answer = qst_statement("What's {} + {} = ".format(a, b))

        # Checks if the answer is correct to the preceding question
        if answer == total:
            # Win statement
            win_counter += 1
            print("correct\n")
        else:
            # Lose statement
            print("Incorrect, the answer was {}\n".format(total))

        # Prints how many games won/lost
        print("WON: {}  |  LOST: {}\n".format(win_counter, round_counter - win_counter))
    # Loop of function
    keep_going = input("press <enter> to play again or any other key to stop")
