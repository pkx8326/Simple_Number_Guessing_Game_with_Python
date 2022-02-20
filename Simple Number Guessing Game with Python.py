#!/usr/bin/env python
# coding: utf-8

# In[82]:


import random

playagain = ""
while playagain not in ("N","n"):
    rand_num = random.randint(1,100)
    print("Welcome to the 1 - 100 Number Guessing Game!")
    level = ""
    while level not in ('1','2'):
        level = input("Input 1 for 'easy' or 2 for 'hard':")

    if level == '1':
        guesses = 10
    else:
        guesses = 5

    get_num = 0
    while get_num != rand_num and guesses > 0:
        try:
            get_num = int(input("Guess a number: "))

            while get_num > 100 or get_num < 1:
                print("Try inputting a number within 1 - 100 range!")
                get_num = int(input("Guess a number: "))

            if get_num > rand_num:
                print("Too high")
                guesses -= 1
                if guesses > 1:
                    print(f"You have {guesses} guesses left.")
                else:
                    print(f"You have {guesses} guess left.")
            elif get_num < rand_num:
                print("Too low")
                guesses -= 1
                if guesses > 1:
                    print(f"You have {guesses} guesses left.")
                else:
                    print(f"You have {guesses} guess left.")
            else:
                print("You've got it!")
                guesses -= 1
                if guesses > 1:
                    print(f"You have {guesses} guesses left.")
                else:
                    print(f"You have {guesses} guess left.")
        except ValueError and get_num > 100:
            print("Input only numbers 1 - 100!")

    while playagain not in ("Y","y","N","n"):
        playagain = input("Play again? Y/N:")


# In[ ]:




