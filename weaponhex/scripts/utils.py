# helper functions for ../weaponhex.py

from os import system as run
from platform import platform as uname 

from constants import BANNER

# clear screen
def clearScreen():
    run('cls' if 'win' in uname().lower() else 'clear')

# clear screen and print banner
def printScreen():
    clearScreen()
    print(BANNER)

