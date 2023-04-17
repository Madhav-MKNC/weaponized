# helper functions for ../weaponhex.py

import os 

from constants import BANNER

# clear screen
def clearScreen():
    os.system("cls" if os.name.lower() == "nt" else "clear")

# clear screen and print banner
def printScreen():
    clearScreen()
    print(BANNER)

# Exit program
def Exit():
    print(f"{GREEN} [Exitting] {WHITE}")
    exit()