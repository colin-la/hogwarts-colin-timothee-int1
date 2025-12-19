import sys
sys.path.append('../')
from utils.input_utils import *
from universe.house import *
from universe.character import *

def meet_friends(character: dict) -> None:
    """
    input : dico character with attributes (like Intelligence, Ambition ...)
    output: same dico but updated with new values
    utilisation : meet_friends({"Ambition":5, "Intelligence":4,...})
    it just make you meet ron hermione draco in the train to Hogwart
    """
    print("You board the Hogwarts Express. The train slowly departs northward...")
    # Ron Weasley
    print("A red-haired boy enters your compartment, looking friendly.")
    print("— Hi! I'm Ron Weasley. Mind if I sit with you?")
    choice = ask_choice("How do you respond?", ["Sure, have a seat", "Sorry, I prefer to travel alone."])    
    attributes = character["Attributes"]
    if choice == 1:
        attributes["Loyalty"] += 1
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
    else :
        attributes["Ambition"] += 1
        print("Ron just ignore you")
    # Hermione Granger
    print("A girl enters next, already carrying a stack of books.")
    print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    choice = ask_choice("How do you respond?", ["Yes, I love learning new things!", "Uh… no, I prefer adventures over books."])
    if choice == 1:
        attributes["Intelligence"] += 1
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
    else :
        attributes["Courage"] += 1
        print("Hermione: — No problem, i will read it alone")
    # Draco Malfoy
    print("Then a blonde boy enters, looking arrogant.")
    print("— I'm Draco Malfoy. It's best to choose your friends carefully from the")
    print("start, don't you think")
    choice = ask_choice("How do you respond?", ["Shake his hand politely.", "Ignore him completely.", "Respond with arrogance."])
    if choice == 1:
        attributes["Ambition"] += 1
        print("Draco smiles: — You will be my best friend from now on !")
    elif choice == 2:
        attributes["Loyalty"] += 1
        print("Draco frowns, annoyed. — You'll regret that!")
    else :
        attributes["Courage"] += 1
        print("You: — You should probably find better approch to make friends you looser")
    # End
    print("The train continues its journey. Hogwarts Castle appears on the horizon...")
    print("Your choices already say a lot about your personality!")
    print("Your updated attributes: ", end="")
    display_character(character)

def welcome_message() -> None:
    print("An old man approch you.")
    print("Pr. Dumbledore: — Hi ! I'm Professor Dumbledore and i will be your main teacher")
    print("Pr. Dumbledore: — If you have any question, don't be afraid to ask me")
    input("Press Enter to continue ...")

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
    print("The sorting ceremony begins in the Great Hall...")
    print("The Sorting Hat observes you for a long time before asking its questions:")
    character["House"] = assign_house(character, questions)
    house = character["House"]
    print(f"The Sorting Hat exclaims: {house}!!!")
    print(f"You join the {house} students to loud cheers!")
    return character["House"]
    
def enter_common_room(character) -> None: 
    print("You follow the prefects through the castle corridors...")
    info_house = load_file("../data/houses.json")[character["House"]]
    print(info_house["description"])
    print(info_house["installation_message"])
    print("Your house colors:", end="")
    for x in info_house["colors"]:
        print(x, end=" ")
    
def start_chapter_2(character) -> int:
    meet_friends(character)
    welcome_message()
    sorting_ceremony(character)
    # installation_message(character)
    enter_common_room(character)
    display_character(character)
    print("This is the end of chapter 2.")
    print("Now, get your pens out and let's start classes !")
    





if __name__ == "__main__":
    print(f"launch from {__file__}")
    character = {"Attributes": {"Intelligence": 5, "Ambition": 2, "Loyalty":3, "Courage": 2}}
    start_chapter_2(character)