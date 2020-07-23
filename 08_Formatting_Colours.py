# Component 8 (2) - Formatting to make game presentable
# Component purpose is to present questions, results etc neatly and organised so the user can identify each statement
# easily. Component includes colour and "border" statements that will be used in the **final product**.

# Import random - for random colour
import random

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

# Used for random colour variables (like a rainbow) (experimental
colour_list = ["red", "green", "gold", "dblue", "pink", "lblue", "grey"]

print("{}Black = 30 ".format(black),
      "{}Red = 31 {}Green = 32 {}Gold/Yellow = 33 ".format(red, green, gold),
      "{}Dark Blue = 34 {}Pink = 35 {}Light Blue = 36 {}Grey = 37 ".format(dblue, pink, lblue, grey))