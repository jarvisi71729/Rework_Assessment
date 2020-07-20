# Component three, round counter when round counter reaches a specific amount stops the program


# Component one, Number checker for round input statement


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

    rounds = num_check("How many questions would you like to answer? (20 max) >>> ", 3, 20)

    # Sets counters to 0
    round_counter = 0

    # Waits for the number of rounds played reach number of rounds needed to play then stop the game
    while round_counter < rounds:

        # Adds a +1 round counter at the start of each round
        round_counter += 1

        # Prints the current round that the user is on
        print("Round ({})\n".format(round_counter))

        # Asks question
        answer = qst_statement("What's 6.01 + 4.23 = ")

        # Checks if the answer is correct to the preceding question
        if answer == 10.24:
            # Win statement
            print("Correct\n")
        else:
            # Lose statement
            print("You lost\n")
    # Loop of function
    keep_going = input("Press <enter> to play again or any key to stop. >>> ")
