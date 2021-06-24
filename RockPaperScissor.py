# Program to run a rock, paper, scissors game.

import random

while True:
    print("Make your choice: ")
    choice=input()
    choice=choice.lower()
    print("My choice is", choice)
    choices=['rock', 'paper', 'scissors']
    computer_choice=choices[random.randint(0,len(choices)-1)]
    print("Computer choice is",computer_choice)
    if choice=='rock':
        if computer_choice=='rock':
            print('It is a tie')
        elif computer_choice=='paper':
            print('You lose, Sorry')
        elif computer_choice=='scissors':
            print('You win, Congrats')
    elif choice=='paper':
        if computer_choice=='paper':
            print('It is a tie')
        elif computer_choice=='scissors':
            print('You lose, Sorry')
        elif computer_choice=='rock':
            print('You win, Congrats')
    elif choice=='scissors':
        if computer_choice=='scissors':
            print('It is a tie')
        elif computer_choice=='rock':
            print('You lose, Sorry')
        elif computer_choice=='paper':
            print('You win, Congrats')
    else:
        print('Invalid Input')
    print()