from random import randint

from universe.house import *
from utils.input_utils import *
from universe.character import *

def learn_spells(character: dict, file_path="data/spells.json") -> None:
    print("You begin your magic lessons at Hogwarts...")
    list_of_spells = load_file(file_path)
    quota = {"Offensive": 1, "Defensive": 1, "Utility": 3}
    current_spells_types = {"Offensive": 0, "Defensive": 0, "Utility": 0} # keeps track of the spells (to meet the quota)
    while current_spells_types != quota:
        random_spell = list_of_spells[randint(0, len(list_of_spells)-1)]
        while (current_spells_types[random_spell["type"]] >= quota[random_spell["type"]]):
            random_spell = list_of_spells[randint(0, len(list_of_spells)-1)]
        add_item(character, "Spells", random_spell['name'])
        print("You have just learned the spell: {} ({})".format(random_spell["name"], random_spell["type"]))
        input("Press Enter to continue...")
        current_spells_types[random_spell["type"]] += 1
    print('\nYou have completed your basic spell training at Hogwarts!\nHere are the spells you now master:\n')
    for spell in character['Spells']:
        spell_type = ''
        spell_description = ''
        for item in list_of_spells:
            if item['name'] == spell:
                spell_type = item['type']
                spell_description = item['description']
        print("- {} ({}): {}".format(spell, spell_type, spell_description))


def magic_quiz(character, file_path="data/magic_quiz.json") -> int:
    """
    plays the scenario of the magic quiz and returns the amount of points scored
    """
    print('Wellcome to the Hogwarts magic quiz!\nAnswer the 4 questions correctly to earn points for your house.\n')
    questions_log = []
    questions = load_file(file_path)
    score = 0
    for i in range(4):
        random_question = questions[randint(0, len(questions)-1)]
        while random_question in questions_log:
            random_question = questions[randint(0, len(questions)-1)]
        answer = ask_text('{}. {}'.format(i+1, random_question['question']))
        if answer != random_question['answer']:
            print("Wrong answer. The correct answer was:", random_question['answer'])
        else:
            print("Correct answer! +25 points for your house.")
            score += 25
        questions_log.append(random_question)
    print("Score obtained:", score, "points")
    return score


def start_chapter_3(character, houses):
    learn_spells(character)
    input("\nPlease press enter to continue...")
    update_house_points(houses, character['House'], magic_quiz(character))
    display_winning_house(houses)
    input("\nPlease press enter to continue...")
    display_character(character)
    input("\nPlease press enter to continue...")



if __name__ == "__main__":
    print(f"launch from {__file__}")
    choice = input("test 1: learn spells or 2: magic_quiz")
    if choice == '1':
        learn_spells(init_character("Potter", "Harry", {}))
    elif choice == '2':
        magic_quiz(init_character("Potter", "Harry", {}))
