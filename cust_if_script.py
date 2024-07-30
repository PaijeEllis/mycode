#!/usr/bin/env python 3
"""Hurricane Scale
    if, elif, else - A simple program using conditionals to make a decision."""


message = 'The Severity of this Hurricane is '


# wrap connection in a float() to accept decimals as numbers

connection = float(input("What is the score?"))


# if input value was higher or equal to 100
if connection >= 100:
    message = message + 'A'
elif connection >= 89:
    message = message + 'B'
elif connection >= 79:
    message = message + 'C'
elif connection >= 69: 
    message = message + 'D'
else:
    message = message + 'F'
print(message)
