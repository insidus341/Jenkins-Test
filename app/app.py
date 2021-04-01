"""Lets goooooo."""
import os
import time
import core.functions as functions

SUMMAGE = functions.add_two_numbers(40, 2)
FILE = os.getcwd() + "/output.txt"

try:
    with open(FILE, "w") as f:
        f.write(str(SUMMAGE))

except FileNotFoundError:
    print("There was an error")

time.sleep(60)
