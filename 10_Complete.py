# Final component

import time
import random


# number checking function for round input


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
            print("Invalid input, try again\n")


# design function to make code appear more sorted


def statement_look(statement, char):
    # Adds a break when the statement is printed in this format
    print()

    # number of characters of statement for top row of the statement
    print(char * len(statement))
    print(statement)

    # number of characters of statement for bottom row of the statement
    print(char * len(statement))


rules = "Welcome to a simple addition game.\nAll answers are below 200\nYou can choose to answer 3 to 20 questions\n"
print(rules)
keep_going = ""
while keep_going == "":

    # How many rounds user is going to play, range between 1 and 20
    # So user doesn't make a game too long
    # So doesn't break the game due to entering 0 or a negative number as the game will instantly end

    rounds = num_check("Questions: ", 3, 20)

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

        # Generates the numbers at the the start of each round
        a = round(random.uniform(1, 100), 2)
        b = round(random.uniform(1, 100), 2)

        # Sum of the preceding random numbers
        total = round(a + b, 2)

        # Adds a +1 round counter at the start of each round
        round_counter += 1

        # Prints the current round that the user is on
        statement_look("Question ({})".format(round_counter), "—")

        question = "{:.2f} + {:.2f} = ".format(a, b)

        # Asks question
        answer = qst_statement("\nWhat is {}".format(question))

        # Collects your answer for the end of game stats to show what you answered
        your_answer.append(answer)

        # Checks if the answer is correct to the preceding question
        if answer == total:
            # +1 counter to win
            win_counter += 1

            # Collects the round info
            won_lost.append('correct')
            # Win statement
            print("Correct\n")

        else:
            # Collects the round info
            won_lost.append('incorrect, should be {}'.format(total))
            # Lose statement and prints the correct answer
            print("Incorrect, the correct answer was {}".format(total))

        # Collects round info when you win a game
        correct_answers.append(total)

        # Collects the question of each round to show the end game stats
        question_stats.append(question)

        # Prints end of round results showing how much games you won and lost
        statement_look("Correct: {}  |  Incorrect: {}".format(win_counter, (round_counter - win_counter)), "—")

    print()

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
    print("Your win percentage for the quiz was {:.2f}%".format(100*(win_counter/rounds)))

    # Loop of function to start and play again
    print()
    keep_going = input("press <enter> to play again or any other key to stop")
print("\nYou have finished the game, thank you for playing!")
