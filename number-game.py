
# Developed by "Reza Heiadrgholizadeh"

import random
import os

############################################

############################################

# main

# loop try again
while True:

    # loop get minimum number
    while True:
        minimum = int(input("Enter the Number Minimum ---- > Minimum >= 0:"))
        if (minimum < 0):
            print("you enter Minimum <0 (Minimum your = {})".format(minimum))
            continue
        break

    # loop get maximum number
    while True:
        maximum = int(input("Enter the Number Maximum ---- > Maximum > Minimum:"))
        if (minimum > maximum):
            print("you enter Maximum < Minimum (Maximum your = {})".format(maximum))
            continue
        break

    num = random.randint(minimum, maximum)
    #print(num)

    while True:
        forcast = int(input("forecasting you from Number:"))
        if ( forcast == num ):
            print("You won the game.")
            break
        elif (forcast > num):
            print("random number < {}".format(forcast))
        elif (forcast < num):
            print("random number > {}".format(forcast))
        else:
            print("number({}) input is not valid.".format(forcast))

    # loop get [Y/N]
    while True:
        try_again = str(input("You want to play again[Y/N]:"))
        if ( try_again.lower() == "y"):
            os.system('cls' if (os.name == 'nt') else 'clear')
            break
        elif (try_again.lower() == "n"):
            exit(0)
        else:
            print("Error: string input is not valid.")
