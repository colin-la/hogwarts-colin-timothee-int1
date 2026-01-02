def init_character(last_name: str, first_name: str, attributes: dict) -> dict:
    dico = {}
    dico["Last Name"] = last_name
    dico["First Name"] = first_name
    dico["Money"] = 100
    dico["Inventory"] = []
    dico["Spells"] = []
    dico["Attributes"] = attributes
    return dico

def display_character(character: dict) -> None:
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
            print(", ".join(current_list))
        else:
            print(character[key])

def modify_money(character: dict, amount: int) -> None:
    character["Money"] += amount

def add_item(character: dict, key: str, item: str) -> None:
    if not(key in ["Inventory", "Spells"]):
        raise TypeError("Key must be either 'Inventory' or 'Spells'")
    else:
        character[key].append(item)


if __name__ == '__main__':
    Harry = init_character("Potter", "Harry", {"Courage": 8, "Intelligence": 8, "Loyalty": 8, "Ambition": 8})
    print('\n\n\n INIT TESTS RUN SUCCESSFULLY\n\n')
    display_character(Harry)
    print('\n\n\n DISPLAY TESTS RUN SUCCESSFULLY\n\n')

    try:
        add_item(Harry, "Money", "10")
        raise 'add_item should make an error with the wrong key'
    except TypeError:
        print("\n\n\nADD_ITEM VALUE TEST RUN SUCCESSFULLY\n\n")

    modify_money(Harry, 10)
    add_item(Harry, "Spells", "tortion_testicular")
    display_character(Harry)
    print('\n\n\n ADD_ITEM AND MONEY TESTS RUN SUCCESSFULLY\n\n')
