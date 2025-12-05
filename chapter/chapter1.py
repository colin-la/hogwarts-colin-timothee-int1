import sys
sys.path.append('../')

from universe.character import * 
from utils.input_utils import *

def introduction():
    input("Welcome to you, stranger. You will live an amazing story \n \
    Without further a do, let's get started ! \n \
    Press Enter to continue ...")

def create_character():
    last_name = ask_text("Enter your character's last name: ")
    first_name = ask_text("Enter your character's first name: ")
    print("Choose your attributes: ")
    courage = ask_number("Courage level (1-10): ")
    intelligence = ask_number("Intelligence level (1-10): ")
    loyalty = ask_number("Loyalty level (1-10): ")
    ambition = ask_number("Ambition level (1-10): ")
    print(f"Character profile: \n \
        Last name: {last_name} \n \
        First name: {first_name} \n \
        Money: 100 \n \
        Inventory: \n \
        Spells: \n \
        Attributes: \n \
        \t - Courage: {courage} \n \
        \t - Intelligence {intelligence}")


def receive_letter():
    pass 

def meet_hagrid(character):
    pass

def buy_supplies(character):
    pass

def start_chapter_1():
    pass

if __name__ == "__main__":
    introduction()
    create_character()