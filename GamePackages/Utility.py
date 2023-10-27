import sys
import random

def exit_program():
    print("The world still needs you.  Come back!")
    sys.exit()

def dice_roller(low, high):
    roll = random.randint(low, high)
    return roll