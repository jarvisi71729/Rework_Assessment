# Component number 9, making the game easier to read
import random


def statement_look(statement, char):
    # Adds a break when the statement is printed in this format
    print()

    # number of characters of statement for top row of the statement
    print(char * len(statement))
    print(statement)

    # number of characters of statement for bottom row of the statement
    print(char * len(statement))


# Gets 2 random numbers of different character lengths
number_1 = random.randrange(1, 1000)
number_2 = random.uniform(1, 10)

# Prints the 2 random numbers with the format and has a dash above and below the statement
statement_look("Random number: {}".format(number_1), "—")
statement_look("Random number: {}".format(number_2), "—")

statement_look("Random number: {}".format(number_1), "-")
statement_look("Random number: {}".format(number_2), "-")
