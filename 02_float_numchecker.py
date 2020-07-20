# Component two, function that allows user to enter whole and decimal point numbers


def qst_statement(question):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print("Invalid input, try again")


# Loop for testing purpose
keep_going = ""
while keep_going == "":

    answer = qst_statement("What's 6.01 + 4.23 = ")
    if answer == 6.01 + 4.23:
        print("Correct")
    else:
        print("Incorrect, the answer was {}".format(6.01 + 4.23))

    keep_going = input("Press <enter> to keep going or any key to stop. >>> ")
