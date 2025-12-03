import json

def ask_text(message: str) -> str:
    """
    texte = ask_text("le message en question")
    """
    anwser = ""
    while anwser == "":
        anwser = str(input(message+" ")).strip()
    return anwser



def ask_number(message: str, min_val=None, max_val=None) -> int:
    """
    number = ask_number("le message en question", 1, 10)
    """
    anwser = min_val - 1
    while not (min_val <= anwser <= max_val):
        try:
            anwser = int(input((message)))
        except:
            anwser = min_val - 1


def ask_choice(message: str, options: list) -> int:
    """
    choix = ask_choice("le message en question", ["oui", "non", "jsp"])
    """
    print(message)
    for x in range(len(options)):
        print(f"{x+1}. {options[x]}")
    result = ask_number("Your choice: ", 1, len(options))
    return result


def load_file (file_path: str):
    """
    data = load_file("le/chemin/du/fichier.json")
    """
    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)



if __name__ == "__main__":
    choice = ask_number("Courage level (1-10): ", 1, 10)
    choice2 = ask_choice("Do you want to continue ? ", ["Yes", "No"])
    print(load_file("../data/inventory.json"))