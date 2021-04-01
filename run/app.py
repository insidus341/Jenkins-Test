"""Lets goooooo."""
import os
import time
import run.core.functions as functions

summage = functions.add_two_numbers(40, 2)

file = os.getcwd() + "/output.txt"
try:
    with open(file, "w") as f:
        f.write(str(summage))

except Exception as e:
    print(e)

time.sleep(60)
