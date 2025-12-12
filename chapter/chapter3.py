from random import randint
from utils.input_utils import *
from universe.character import *

def learn_spells(character: dict, file_path="../data/spells.json"):
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


if __name__ == "__main__":
    print(f"launch from {__file__}")
    learn_spells(init_character("Potter", "Harry", {}))
