# Component 8 (1) - Formatting to make game presentable
# Component purpose is to present questions, results etc neatly and organised so the user can identify each statement
# easily. Component includes colour and "border" statements that will be used in the **final product**.

# Imports random - for random number generator
import random


# Statement character function for presentation / organisation
# Character function presents statements with a row of characters below and above to seperate information from other
# statements used in final game code


def statement_look(statement, char):
    # Separates statements
    print()

    # Top row of characters 1 line above statement
    print(char * len(statement))

    print(statement)

    # Top row of characters 1 line above statement
    print(char * len(statement))


# Generates 2 random numbers for different character lengths
number_1 = random.randrange(1, 1000)
number_2 = random.uniform(1, 10)

# Statement is generated with selected 'symbols' above and below information
statement_look("Character length: {}".format(number_1), "=")

statement_look("Character length: {}".format(number_2), "—")

statement_look("Character length: {}".format(number_1), "-")

statement_look("Character length: {}".format(number_2), "\/")


