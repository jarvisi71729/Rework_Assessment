# Component one, Number checker for round input statement


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

# How many rounds user is going to play, range between 1 and 20
# So user doesn't make a game too long
# So doesn't break the game due to entering 0 or a negative number as the game will instantly end


question = num_check("How many questions would you like to answer? (20 max) >>> ", 3, 20)
print("Question: {}".format(question))
