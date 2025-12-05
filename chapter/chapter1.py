import sys
sys.path.append('../')

from universe.character import * 
from utils.input_utils import *

def introduction():
    input("Welcome to you, stranger. You will live an amazing story \nWithout further a do, let's get started ! \nPress Enter to continue ...")

def create_character():
    last_name = ask_text("Enter your character's last name: ")
    first_name = ask_text("Enter your character's first name: ")
    print("Choose your attributes: ")
    courage = ask_number("Courage level (1-10): ", 1, 10)
    intelligence = ask_number("Intelligence level (1-10): ", 1, 10)
    loyalty = ask_number("Loyalty level (1-10): ", 1, 10)
    ambition = ask_number("Ambition level (1-10): ", 1, 10)
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
    print("An owl flies through the window, delivering a letter sealed with the Hogwarts crest...")
    print("“Dear Student,\n")
    print("We are pleased to inform you that you have been accepted to Hogwarts")
    print("School of Witchcraft and Wizardry!”\n")
    choice = ask_choice("Do you accept this invitation and go to Hogwarts?\n", ["Yes, of course!", "No, I'd rather stay with Uncle Vernon..."])
    if choice == 1:
        print("Thank you, we'll be waiting you on the platform 9 and 3/4")
        print("in order to take the Hogwarts Express")
        
    if choice == 2:
        print("You tear up the letter, and Uncle Vernon cheers:")
        print("“EXCELLENT! Finally, someone NORMAL in this house!”")
        print("The magical world will never know you existed... Game over")
        sys.exit()

def meet_hagrid(character):
    pass

def buy_supplies(character):
    pass

def start_chapter_1():
    pass

if __name__ == "__main__":
    introduction()
    create_character()
    receive_letter()