import sys
from utils.input_utils import *
from universe.house import *
from universe.character import *

def meet_friends(character: dict) -> None:
    print_slow("You board the Hogwarts Express. The train slowly departs northward...")
    print_slow("A red-haired boy enters your compartment, looking friendly.")
    print_slow("— Hi! I'm Ron Weasley. Mind if I sit with you?")
    choice = ask_choice("How do you respond?", ["Sure, have a seat", "Sorry, I prefer to travel alone."])    
    attributes = character["Attributes"]
    if choice == 1:
        attributes["Loyalty"] += 1
        print_slow("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
    else :
        attributes["Ambition"] += 1
        print_slow("Ron just ignore you")
    print_slow("A girl enters next, already carrying a stack of books.")
    print_slow("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    choice = ask_choice("How do you respond?", ["Yes, I love learning new things!", "Uh… no, I prefer adventures over books."])
    if choice == 1:
        attributes["Intelligence"] += 1
        print_slow("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
    else :
        attributes["Courage"] += 1
        print_slow("Hermione: — No problem, i will read it alone")
    print_slow("Then a blonde boy enters, looking arrogant.")
    print_slow("— I'm Draco Malfoy. It's best to choose your friends carefully from the")
    print_slow("start, don't you think")
    choice = ask_choice("How do you respond?", ["Shake his hand politely.", "Ignore him completely.", "Respond with arrogance."])
    if choice == 1:
        attributes["Ambition"] += 1
        print_slow("Draco smiles: — You will be my best friend from now on !")
    elif choice == 2:
        attributes["Loyalty"] += 1
        print_slow("Draco frowns, annoyed. — You'll regret that!")
    else :
        attributes["Courage"] += 1
        print_slow("You: — You should probably find better approch to make friends you looser")
    print_slow("The train continues its journey. Hogwarts Castle appears on the horizon...")
    print_slow("Your choices already say a lot about your personality!")
    print("Your updated attributes: ", end="")
    display_character(character)

def welcome_message() -> None:
    print_slow("An old man approch you.")
    print_slow("Pr. Dumbledore: — Hi ! I'm Professor Dumbledore and i will be your main teacher")
    print_slow("Pr. Dumbledore: — If you have any question, don't be afraid to ask me")

def sorting_ceremony(character) -> int:
    questions = [
                    (
                        "You see a friend in danger. What do you do?",
                        ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
                        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
                    ),
                    (
                        "Which trait describes you best?",
                        ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
                        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
                    ),
                    (
                        "When faced with a difficult challenge, you...",
                        ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends","Analyze the problem"],
                        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
                    )
                ]
    print_slow("The sorting ceremony begins in the Great Hall...")
    print("The Sorting Hat observes you for a long time before asking its questions:")
    character["House"] = assign_house(character, questions)
    house = character["House"]
    print_slow(f"The Sorting Hat exclaims: {house}!!!")
    print_slow(f"You join the {house} students to loud cheers!\n")
    return character["House"]
    
def enter_common_room(character) -> None: 
    print_slow("You follow the prefects through the castle corridors...")
    info_house = load_file("data/houses.json")[character["House"]]
    print_slow(info_house["description"])
    print_slow(info_house["installation_message"])
    print_slow("Your house colors:", end="")
    for x in info_house["colors"]:
        print_slow(x, end=" ")
    
def start_chapter_2(character) -> None:
    meet_friends(character)
    press_enter_to_continue()
    os.system("cls")
    welcome_message()
    press_enter_to_continue()
    sorting_ceremony(character)
    press_enter_to_continue()
    os.system("cls")
    enter_common_room(character)
    display_character(character)
    print_slow("This is the end of chapter 2 !")
    print_slow("Now, get your pens out and let's start classes !")
    press_enter_to_continue()
    os.system("cls")
    





if __name__ == "__main__":
    print(f"launch from {__file__}")
    character = {"Attributes": {"Intelligence": 5, "Ambition": 2, "Loyalty":3, "Courage": 2}}
    start_chapter_2(character)