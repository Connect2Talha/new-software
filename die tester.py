#1/usr/bin/env python3

from random import randint
from typing import Any

from win32serviceutil import usage


def roll_dice():

    return randint(1, 6)

for _ in range(10):
    print(roll_dice())


 # Generate Target Number (17 and 29)

def generate_target_number(lower_limit=17, upper_limit=29):
    return randint(lower_limit, upper_limit)

if __name__ == '__main__':
     generate_target_number()

     print(f'target number : {generate_target_number()}')
     print()


     total=0


    while True:


    this_roll = roll_dice()

    total += this_roll

     print(f'you rolled {this_roll}). your total is {total}.')

     again = input('do you want to roll again? (y/n) ')
     if again == 'n':

     break


