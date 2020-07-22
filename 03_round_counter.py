# Component three - round counter
# Checks user input is within range (3, 20)
# Checks user input is a number


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


rounds = num_check("How many questions would you like to answer? (20 max) >>> ", 3, 20)
# Set round counter to zero, 1 round will be added before each question
rounds_counter = 0

# To make sure game finishes when user plays all desired rounds
while rounds_counter < rounds:
    # Prints round counter so user can easily keep track
    print("Round {}".format(rounds_counter + 1))
    # Adds one round (+1 to counter) before each question is printed
    rounds_counter += 1
    print("Question 1:\n...")

# Farewells user
print("Thank you for playing!")
