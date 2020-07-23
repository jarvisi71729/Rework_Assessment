# Component six - end of game results
# Component purpose is to organise and print user's question history with correct or wrong statements
# NOTE - from this component (6) and onwards, I switched from using a range of random numbers from 1 - 100 with 2dp
#        to a range of *whole* random numbers from -100 - 100. This decision was made after receiving feedback about
#        random numbers with decimals being too ~hard~

# Imports random for random number generator
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

# Begins keep going loop if user wants to play again at the end of the game
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

        # Random number generator used for questions
        # Generates two random numbers that will be used in question statement, *prints numbers for testing purposes*
        a = round(random.uniform(1, 100))
        print("#1 - {}".format(a))

        b = round(random.uniform(1, 100))
        print("#2 - {}".format(b))

        # Total sum of random numbers above, printed for testing purposes
        total = round(a + b)
        print("Total = {}\n".format(total))

        # Adds one (+1 to counter) round before each question is printed
        round_counter += 1

        # Prints round counter so user can easily keep track
        print("Question ({})\n".format(round_counter))

        # Question statement using randomly generated numbers
        question = "{} + {} = ".format(a, b)

        # Prints question statement for user to answer
        answer = qst_statement("{}".format(question))

        # HERE <<<<<<<<<<<<<<<

        # Grabs your answer for game stats at the end of the game (will print answer if user guesses answer incorrectly)
        your_answer.append(answer)

        # Checks if user input is correct (same as total sum of 2 numbers)
        if answer == total:
            # Adds +1 to win counter if user input is correct
            win_counter += 1

            # Prints win result if user is correct, adds 'correct' data for end game stats
            won_lost.append('Correct')
            print("Correct\n")

        else:
            # Prints lose result if user is wrong and prints correct answer
            won_lost.append('Incorrect, should be {}'.format(total))

        # Grabs round info - if user gets answer correct
        correct_answers.append(total)

        # Grabs question # for end game results (question number will be presented before results for user to keep track
        # of what they got wrong/correct easily)
        question_stats.append(question)

        # Prints user game results (how many wins & losses)
        print("WON: {}  |  LOST: {}\n".format(win_counter, (round_counter - win_counter)))

    # End game stats - question #, win/loss result (if user gets question incorrect, answer will be printed)
    list_count = 1
    for i in range(len(correct_answers)):

        # End game stats - questions, followed by results
        print("Question {}: {}{} \t({})".format(list_count, question_stats[i], your_answer[i], won_lost[i]))

        # Questions: (following)
        list_count += 1

    print()

    # Win percentage (wins / total rounds)
    print("Your win percentage for this game was {:.2f}%".format(100*(win_counter/rounds)))

    # Asks user if they want to play another set of rounds or stop
    print()
    keep_going = input("Press <enter> to play again or any key to stop. >>> ")
