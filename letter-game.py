
# Developed by "Reza Heiadrgholizadeh"

import random
import os

############################################
def show_charaters(word ,i ,n ,m_list):
    os.system('cls' if (os.name == 'nt') else 'clear')
    #print("word------->{}".format(word))
    #print("list------{}".format(m_list))
    out_word = ""
    if (len(m_list) > 0):
        for j in range(len(word)):
            tmp = False
            for h in range(len(m_list)):
                if ( word[j].lower() == m_list[h]):
                    #print(word[j] ,end='')
                    out_word += (word[j])
                    tmp = True
                    break
            if ( not tmp):
                #print("_" ,end='')
                out_word += ("_")
    else:
        for _ in range(len(word)):
            #print("_" ,end='')
            out_word += ("_")
    print(out_word)
    print("\n")
    print("{}\{}".format(i ,n))
    return out_word

############################################

# main

# loop try again
while True:
    n = int(input("The number of predictions that you want to guess:"))
    words = ( 'security',
              'pliocy',
              'physics',
              'chemistry',
              'apple',
              'Grapes',
              'Mango',
              'Date',
              'Cashew',
              'Peanut',
              'Mushroom',
              'Asparagus')

    x = random.randint(0, len(words ) -1)
    word = words[x]
    len_word = len(words[x])
    m_list = []
    flag = False
    for i in range(n):
        out_word = show_charaters(word , i +1 ,n ,m_list)
        if (out_word.lower() == word.lower()):
            flag = True
            break
        char = str(input("inset your character (or forecasting the string):"))
        if (char.lower() == word.lower()):
            flag = True
            break
        else:
            for j in range(len_word):
                if (char.lower() == word[j].lower()):
                    m_list.append(char)
                    break
                else:
                    pass

    if (flag):
        print("You won the game.")
    else:
        print("You missed the game.")

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