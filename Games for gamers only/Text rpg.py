# Python text RPG
#RISHIK

import cmd
import textwrap
import sys
import os
import time
import random

screenWidth = 100

#### PLAYER SETUP #####
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
MyPlayer = player()

#### Title Screen ####
def title_screen_selections():
    option= input("> ")
    if option.lower() == ("play"):
        start_game() #placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower()not in ['play', 'help', 'quit']:
        print("please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()  # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print("###########################")
    print("# Welcome to the Text RPG #")
    print("###########################")
    print("         - Play -          ")
    print("         - Help -          ")
    print("         - Quit -          ")
    print("   Copyright 2020 C.inc    ")
    title_screen_selections()

def help_menu():
    print("###########################")
    print("# Welcome to the Text RPG #")
    print("###########################")
    print("-Use up, down left right to move")
    print("-Type your commands to do them  ")
    print("-Use 'look' to inspect something")
    print("-Good luck and have fun")
    title_screen_selections()


#### GAME FUNCTIONALITY ####
def start_game():

    

#### MAP ####
"""
 a1 a2 a3 a4
_____________
l  l  l  l  l a4
_____________
l  l  l  l  l b4
_____________
l  l  l  l  l c4
_____________
l  l  l  l  l d4
______________
"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False,'a3': False, 'a4': False,
                 'b1': False, 'b2': False,'b3': False, 'b4': False,
                 'c1': False, 'c2': False,'c3': False, 'c4': False,
                 'd1': False, 'd2': False,'d3': False, 'd4': False,
                 }
