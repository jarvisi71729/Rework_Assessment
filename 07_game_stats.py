# Component seven, match history to compare answers to what user inputs

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
    win_counter = 0

    # Collection of stats
    correct_answers = []
    question_stats = []
    your_answer = []
    won_lost = []

    # Waits for the number of rounds played reach number of rounds needed to play then stop the game
    while round_counter < rounds:

        # # Generates and prints the numbers at the the start of each round. (prints for testing purposes)
        a = round(random.uniform(1, 100), 2)
        # print("#1 = {}".format(a))
        b = round(random.uniform(1, 100), 2)
        # print("#2 = {}".format(b))
        #
        # # Sum of the preceding random numbers
        total = round(a + b, 2)
        #
        # print("Total = {:.2f}\n".format(total))

        # Adds a +1 round counter at the start of each round
        round_counter += 1

        # Prints the current round that the user is on
        print("Question ({})\n".format(round_counter))

        question = "{:.2f} + {:.2f} = ".format(a, b)

        # Asks question
        answer = qst_statement("What's {}".format(question))

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
