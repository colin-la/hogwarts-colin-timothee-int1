def init_character(last_name: str, first_name: str, attributes: dict) -> dict:
    """
    function returning a dictionary of a new character using his last name, first name and a dictionary of attributes
    """
    dico = {}
    dico["Last Name"] = last_name
    dico["First Name"] = first_name
    dico["Money"] = 100
    dico["Inventory"] = []
    dico["Spells"] = []
    dico["Attributes"] = attributes
    return dico

def display_character(character: dict) -> None:
    """
    function displaying everything about a character passed as a parameter (dictionary)
    """
    print("Character profile:")
    for key in character:
        print(key + ":", end=' ')
        if type(character[key]) is dict:
            print()
            for key2, value2 in character[key].items():
                print(" - {}: {}".format(key2, value2))
        elif type(character[key]) is list:
            current_list = character[key]
            for i in range(len(current_list)):
                current_list[i] = str(current_list[i])
            print("".join(current_list))
        else:
            print(character[key])

#################
##### Tests #####
#################
'''
display_character(init_character("Potter", "Harry", {"Courage": 8, "Intelligence": 8, "Loyalty": 8, "Ambition": 8}))
'''