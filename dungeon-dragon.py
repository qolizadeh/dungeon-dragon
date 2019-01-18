# Developed by "Reza Heiadrgholizadeh"

import random
import os

############################################

def draw(x, y, n):
    os.system('cls' if (os.name == 'nt') else 'clear')
    for _ in range(n):
        print(" _", end='')
    print("")
    for i in range(n):
        for j in range(n):
            if ((i + 1 == x) & (j + 1 == y)):
                print("|X", end='')
            else:
                print("|_", end='')
        print("|")
    print("")


############################################

# main

# loop try again
while True:

    # loop number matrix
    while True:
        n = int(input("Enter the Number Matrix Game (NxN) ---- > N >= 3:"))
        if (n < 3):
            print("you enter n <3 (n your = {})".format(n))
            continue
        break

    # loop get random X, Z, D
    while True:
        x_x = random.randint(1, n)
        x_y = random.randint(1, n)

        z_x = random.randint(1, n)
        z_y = random.randint(1, n)

        d_x = random.randint(1, n)
        d_y = random.randint(1, n)

        if (((z_x != x_x) & (z_y != x_y)) &
                ((z_x != d_x) & (z_y != d_y)) &
                ((x_x != d_x) & (x_y != d_y))):
            break

    print("x={},{}".format(x_x, x_y))
    print("z={},{}".format(z_x, z_y))
    print("d={},{}".format(d_x, d_y))

    for _ in range(n):
        print(" _", end='')
    print("")
    for i in range(n):
        for j in range(n):
            if ((i + 1 == x_x) & (j + 1 == x_y)):
                row = x_x
                column = x_y
                print("|X", end='')
            else:
                print("|_", end='')
        print("|")
    print("")

    # loop display text direction X
    while True:
        if (row > 1):
            print("Enter your \"Top\" for top X ")
        if (column < n):
            print("Enter your \"Right\" for right X ")
        if (column > 1):
            print("Enter your \"Left\" for left X ")
        if (row < n):
            print("Enter your \"Down\" for down X ")

        # loop get move X
        while True:
            input_str = str(input("Enter:"))
            if ((input_str.lower() == "top") & (row > 1)):
                row = row - 1
                break
            elif ((input_str.lower() == "down") & (row < n)):
                row = row + 1
                break
            elif ((input_str.lower() == "left") & (column > 1)):
                column = column - 1
                break
            elif ((input_str.lower() == "right") & (column < n)):
                column = column + 1
                break
            else:
                print("Error: string input is not valid.")

        draw(row, column, n)
        if ((row == d_x) & (column == d_y)):
            print("You won the game.")
            break
        elif ((row == z_x) & (column == z_y)):
            print("You missed the game.")
            break
        else:
            continue

    # loop get [Y/N]
    while True:
        try_again = str(input("You want to play again[Y/N]:"))
        if (try_again.lower() == "y"):
            os.system('cls' if (os.name == 'nt') else 'clear')
            break
        elif (try_again.lower() == "n"):
            exit(0)
        else:
            print("Error: string input is not valid.")