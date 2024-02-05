"""
Build a Number guessing game, in which the user selects a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that integer in the
minimum number of guesses

Author: Shravan
Date: 04-02-2024
"""
import random, math

# Taking user input range
try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
except:
    print("Enter a valid integer")

# Randomly choosing a number
target = random.randint(start, end)
guesses = round(math.log(end-start+1, 2))
print("You have only ", guesses, " Attempts to guess.")

countGuess = 0  # counting number of guess
while countGuess<guesses:
    countGuess += 1 # increment
    # User guess
    userInput = int(input("Guess the number: "))
    if userInput==target:
        print(f"Wow you did it in {countGuess} attempts")
        break
    elif target<userInput:
        print("You guessed too high!!")
    else:
        print("You guessed too low!!")
    
if countGuess >= guesses:
    print("\nThe number is %d" % target)
    print("\tBetter Luck Next time!")