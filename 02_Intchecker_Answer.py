# Component two - integer checker
# Checks user input is an integer for

def int_check(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            valid = True
            return response

        except ValueError:
            print("You did not enter an INTEGER. Please try again\n")

# Loop entire game... for testing
keep_going = ""
while keep_going == "":

    answer = int_check("6 + 4 = ")
    if answer == 10:
        print("Correct\n")
    else:
        print("Incorrect, the answer was 10\n")

    keep_going = input("Press <enter> to keep going or any key to stop. >>> ")