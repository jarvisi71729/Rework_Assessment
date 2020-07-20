# Component five, compares answer to input and adds a +1 win counter if you win round

# Number checker functions


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

    rounds = num_check("How many rounds? ", 1, 20)
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

        # Asks question
        answer = qst_statement("What's 4.11 + 3.83 = ")

        # Checks if the answer is correct to the preceding question
        if answer == 7.94:
            # Win statement
            win_counter += 1
            print("correct\n")
        else:
            # Lose statement
            print("Incorrect, the answer was 7.94\n")

        # Prints how many games won/lost
        print("WON: {}  |  LOST: {}\n".format(win_counter, round_counter - win_counter))
    # Loop of function
    keep_going = input("press <enter> to play again or any other key to stop")
