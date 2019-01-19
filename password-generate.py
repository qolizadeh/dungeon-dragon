

# Developed by "Reza Heiadrgholizadeh"

import random
import os
import string
############################################

############################################

# main

while True:
    num = int(input("Enter you number password generate( num >= 1): "))
    if (num >= 1):
        break
    continue


while True:
    length = int(input("Enter you length password generate( len >= 5): "))
    if (length >= 5):
        break
    continue

m_list = list(string.ascii_letters+string.digits+string.punctuation)

for _ in range(num):
    for _ in range(length):
        i = random.randint(0, len(m_list)-1)
        print(m_list[i],end='')
    print("")
