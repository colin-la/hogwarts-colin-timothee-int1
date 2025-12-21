import sys
from utils.input_utils import *
from chapter.chapter1 import *
from time import sleep
from chapter.chapter2 import *
from chapter.chapter3 import *

def display_main_menu() -> int:
    return ask_choice("", ["Start Chapter 1 – Arrival in the magical world.", "Exit the game."])

def launch_menu_choice() -> None:
    houses =  {
 "Gryffindor": 0,
 "Slytherin": 0,
 "Hufflepuff": 0,
 "Ravenclaw": 0
}
    for key in load_file("./data/houses.json").keys():
        houses[key] = 0
    choice = display_main_menu()
    if choice == 1:
        character = start_chapter_1()
        start_chapter_2(character)
        start_chapter_3(character, houses)
        # start_chapter4()
    elif choice == 2:
        print("Too bad... \nGoodbye and see you next time !")
        sleep(2)
        sys.exit()
    return

if __name__ == "__main__":
    launch_menu_choice()