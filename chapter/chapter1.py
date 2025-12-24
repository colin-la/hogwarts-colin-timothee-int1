import sys
sys.path.append('../')

from universe.character import *
from utils.input_utils import *

def introduction():
    print("\n\n")
    print_slow("Welcome to you, stranger. You will live an amazing story")
    print_slow("Without further a do, let's get started !")
    input("Press Enter to continue ...")

def create_character():
    last_name = ask_text("Enter your character's last name: ")
    first_name = ask_text("Enter your character's first name: ")
    print("Choose your attributes: ")
    courage = ask_number("Courage level (1-10): ", 1, 10)
    intelligence = ask_number("Intelligence level (1-10): ", 1, 10)
    loyalty = ask_number("Loyalty level (1-10): ", 1, 10)
    ambition = ask_number("Ambition level (1-10): ", 1, 10)
    dico = init_character(last_name, first_name, {"Courage": courage, "Intelligence": intelligence, "Loyalty":loyalty, "Ambition": ambition})
    display_character(dico)
    return dico
    

def receive_letter():
    print_slow("An owl flies through the window, delivering a letter sealed with the Hogwarts crest...")
    print_slow("“Dear Student,")
    print_slow("We are pleased to inform you that you have been accepted to Hogwarts")
    print_slow("School of Witchcraft and Wizardry!”\n")
    choice = ask_choice("Do you accept this invitation and go to Hogwarts?\n", ["Yes, of course!", "No, I'd rather stay with Uncle Vernon..."])
    if choice == 1:
        print_slow("Thank you, we'll be waiting for you on the platform 9 and 3/4 in order to take the Hogwarts Express")
    if choice == 2:
        print_slow("You tear up the letter, and Uncle Vernon cheers:")
        print_slow("“EXCELLENT! Finally, someone NORMAL in this house!”")
        print_slow("The magical world will never know you existed... Game over")
        sys.exit()

def meet_hagrid(character: dict) -> None:
    choice = ask_choice("Hagrid: 'Hello {}! I’m here to help you with your shopping on Diagon Alley.\n\n\
          Do you want to follow Hagrid?".format(character['First Name']), ["Yes", "No"])
    if choice == 2:
        print_slow("Hagrid gently insists and takes you along anyway!")
    else:
        print_slow("You follow Hagrid to Diagon Alley!")

def buy_supplies(character: dict) -> None:
    print_slow("Welcome to Diagon Alley!\n\nCatalog of available items:")
    dict_items = load_file("data/inventory.json")
    # display item list
    for key, value in dict_items.items():
        if dict_items[key][0] in ["Magic Wand", "Wizard Robe", "Potions Book"]:
            message = " (required)"
        else:
            message = ""
        print("{}. {} - {} Galleons".format(key, dict_items[key][0], dict_items[key][1]) + message)

    # buying required items loop
    required = ["Magic Wand", "Wizard Robe", "Potions Book"]
    while len(required) > 0:
        print("You have", character["Money"], "Galleons.")
        print("Remaining required items: ", end= " ")
        for element in required:
            if element == required[-1]:
                endd = ""
            else:
                endd = ","
            print(element, end=endd)
        print()
        choice = ask_number("Enter the number of the item to buy: ", 1, 8)
        if character["Money"] < dict_items[str(choice)][1]:
            print("\n\n\nYou didn't have enough money to pay and the merchant killed you.")
            print_slow("GAME OVER", 60)
            sys.exit()
            
        # else
        modify_money(character, -1 * dict_items[str(choice)][1])
        if dict_items[str(choice)][0] in required:
            required.remove(dict_items[str(choice)][0])
        print("You bought: {} (-{} Galleons)".format(dict_items[str(choice)][0], dict_items[str(choice)][1]))
        print()
        add_item(character, "Inventory", dict_items[str(choice)][0])
    print("All required items have been purchased!\n")

    # display pet list
    print_slow("It's time to choose your Hogwarts pet!\n")
    input("\nPlease press enter to continue...\n")
    print("You have", character["Money"], "Galleons.\n")
    dict_pet = {
    "1": ["Owl", 20],
    "2": ["Cat",  15],
    "3": ["Rat", 10],
    "4": ["Toad", 5],
}
    # buying the pet
    for key, value in dict_pet.items():
        print("{}. {} - {} Galleons".format(key, dict_pet[key][0], dict_pet[key][1]))
    choice = ask_choice('Which pet do you want?', ["Owl", "Cat", "Rat", "Toad"])
    if character["Money"] < dict_pet[str(choice)][1]:
        print("\n\n\nYou didn't have enough money to pay and the merchant killed you.")
        print_slow("GAME OVER", 60)
        sys.exit()
         
    modify_money(character, -1 * dict_pet[str(choice)][1])
    add_item(character, "Inventory", dict_pet[str(choice)][0])
    print("You chose: {} (-{} Galleons)".format(dict_pet[str(choice)][0], dict_pet[str(choice)][1]))


    # final display of inventory
    print("\nAll required items have been successfully purchased! Here is your final inventory:\n\n")
    display_character(character)

def start_chapter_1() -> dict:
    introduction()
    character = create_character()
    input("\nPlease press enter to continue...")
    receive_letter()
    meet_hagrid(character)
    input("\nPlease press enter to continue...")
    buy_supplies(character)
    print_slow("End of Chapter 1! Your adventure begins at Hogwarts...")
    input("\nPlease press enter to continue...")
    return character


#################
##### Tests #####
#################

if __name__ == "__main__":
    start_chapter_1()
