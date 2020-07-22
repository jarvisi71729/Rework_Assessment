# Component six - end of game results
# Component purpose is to organise and print user's question history with correct or wrong statements

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

    # Game statistics - will collect results at the end of each question for after the game is finished (end results)
    correct_answers = []
    question_stats = []
    your_answer = []
    won_lost = []

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
        print("Question ({})\n".format(round_counter))

        # Question statement using randomly generated numbers
        question = "{:.2f} + {:.2f} = ".format(a, b)

        # Prints question statement for user to answer
        answer = qst_statement("{}".format(question))

        # HERE <<<<<<<<<<<<<<<

        # Collects your answer for the end of game stats to show what you answered
        your_answer.append(answer)

        # Checks if the answer is correct to the preceding question
        if answer == total:
            # +1 counter to win
            win_counter += 1

            # Win statement
            won_lost.append('Correct')
            print("Correct\n")

        else:
            # Lose statement and prints the correct answer

            won_lost.append('Incorrect, should be {}'.format(total))

        # Collects round info when you win a game
        correct_answers.append(total)

        # Collects the question of each round to show the end game stats
        question_stats.append(question)

        # Prints end of round results showing how much games you won and lost
        print("Correct: {}  |  Incorrect: {}\n".format(win_counter, (round_counter - win_counter)))

    # Game history showing if you won/lost the round and prints the question and the answer and shows what user answered
    list_count = 1
    for i in range(len(correct_answers)):

        # Prints game history >>> question number, question itself
        # user answer, win/lost stat if lost print correct answer
        print("Question {}: {}{:.2f} \t({})".format(list_count, question_stats[i], your_answer[i], won_lost[i]))

        # Goes to the next item (next question number)
        list_count += 1

    print()

    # Prints the percentage of how many games you won
    print("Your win percentage for this game was {:.2f}%".format(100*(win_counter/rounds)))

    # Loop of function to start and play again
    print()
    keep_going = input("Press <enter> to play again or any key to stop. >>> ")
