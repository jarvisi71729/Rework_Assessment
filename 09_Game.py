# Final component - end result of assessment (all components together)
# Component purpose is for the user to enjoy the completed game :]

# Experimental - used to slow down printing to give user time to read
import time

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
                print("{}You did not enter a number between {} and {}\n".format(red, low, high))
        except ValueError:
            print("{}Invalid input\n".format(red))

# Checks user input is an integer, only allows whole numbers


def int_check(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            valid = True
            return response

        except ValueError:
            print("{}You did not enter an INTEGER. Please try again\n".format(red))


# Statement character function for presentation / organisation
# Character function presents statements with a row of characters below and above to seperate information from other
# statements used in final game code

def statement_look(statement, char):
    # Separates statements for tidiness
    print()

    # Top row of characters 1 line above statement
    print(char * len(statement))
    print(statement)

    # Top row of characters 1 line above statement
    print(char * len(statement))


# Colour variable: red
black = "\u001b[30m"

# Colour variable: red
red = "\u001b[31m"

# Colour variable: green
green = "\u001b[32m"

# Colour variable: gold / yellow
gold = "\u001b[33m"

# Colour variable: dark blue
dblue = "\u001b[34m"

# Colour variable: pink
pink = "\u001b[35m"

# Colour variable: light blue
lblue = "\u001b[36m"

# Colour variable: grey
grey = "\u001b[37m"

# Colour variable: none
# Format is for breaking colour code and will be used at the end of each statement
# (returning next statement to a neutral colour (black text))
colour_end = "\u001b[0m"


# Rules statement - brief explanation of the game
print(u"{}Welcome to my Math Quiz! \n{}This is an addition game which includes *negative* and *positive* numbers\n"
               "{}Your overall game statistics will be printed at the end of the game for you to read.{}\n".format(pink, lblue, gold, colour_end))
time.sleep(2.5)

# Begins keep going loop if user wants to play again at the end of the game
keep_going = ""
while keep_going == "":

    # Minimum questions (rounds) is 3 instead of 1 so the game doesnt end quickly and gives the user's end results
    # (component 7) variety. Max is set to 20 so the game isn't overly long
    user_rounds = num_check("{}How many questions would you like to answer? (20 max) >>> {}".format(dblue, colour_end), 3, 20)
    time.sleep(1)

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
    while round_counter < user_rounds:

        # Random number generator used for questions
        a = (random.randrange(-100, 100))

        b = (random.randrange(-100, 100))

        # Total sum of random numbers above
        total = (a + b)

        # Adds one (+1 to counter) round before each question is printed
        round_counter += 1

        # Prints round counter so user can easily keep track
        statement_look("Question ({})".format(round_counter), "-")

        # Prints question statement for user to answer
        question = "{}{} + {} = ".format(gold, a, b)

        # Prints question statement for user to answer
        answer = int_check("\n{}{}".format(question, colour_end))

        # Grabs your answer for game stats at the end of the game (will print answer if user guesses answer incorrectly)
        your_answer.append(answer)

        # Checks if user input is correct (same as total sum of 2 numbers)
        if answer == total:
            # Adds +1 to win counter if user input is correct
            win_counter += 1

            # Prints win result if user is correct, adds 'correct' data for end game stats
            won_lost.append('{}Correct{}'.format(green, gold))
            print("{}Congratulations! You got the answer correct.{}\n".format(green, colour_end))

        else:
            # Prints lose result if user is wrong and prints correct answer
            print("{}Sorry, your answer was incorrect.\n".format(red, colour_end))
            won_lost.append('{}Incorrect, the correct answer was {}, bad luck!{}'.format(red, total, gold))

        # Grabs round info - if user gets answer correct
        correct_answers.append(total)

        # Grabs question # for end game results (question number will be presented before results for user to keep track
        # of what they got wrong/correct easily)
        question_stats.append(question)

        # Prints user game results (how many wins & losses)
        print("{}Questions answered {}correctly{}: {}  |  Questions answered {}incorrectly{}: {}{}\n".format(pink, green, pink, win_counter, red, pink, (round_counter - win_counter), colour_end))

    # End game stats - question #, win/loss result (if user gets question incorrect, answer will be printed)
    list_count = 1
    for i in range(len(correct_answers)):
        # End game stats - questions, followed by results
        print("{}For question #{}: {}{} \t({}){}".format(dblue, list_count, question_stats[i], your_answer[i], won_lost[i], colour_end))

        # Questions: (following)
        list_count += 1

    print()

    # Win percentage (wins / total rounds)
    print("{}Your overall win percentage: {:.2f}%{}".format(green, 100 * (win_counter / user_rounds), colour_end))

    # Asks user if they want to play another set of rounds or stop
    print()
    keep_going = input("{}Press <enter> to play again or any key to stop. >>> {}".format(grey, colour_end))
print("{}Thank you for playing :) Come play again soon!".format(pink))
