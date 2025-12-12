import sys
from utils.input_utils import *
from chapter.chapter1 import *
def display_main_menu() -> int:
    return ask_choice("", ["Start Chapter 1 – Arrival in the magical world.", "Exit the game."])

def launch_menu_choice() -> None:
    houses = {}
    choice = display_main_menu()
    if choice == 1:
        dico = start_chapter1()
        # houses = start_chapter2()
        # start_chapter3()
        # start_chapter4()
    elif choice == 2:
        print("Too bad... \nGoodbye and see you next time !")
        sys.exit()

if __name__ == "__main__":
    launch_menu_choice()