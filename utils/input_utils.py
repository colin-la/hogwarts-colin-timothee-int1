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
    renvoie le nombre entré par l'utilisateur 
    Si l'utilisateur n'entre pas un integer ou entre un integer
    en dehors des limites, la fonction re-demande d'entrer un nombre
    """
    try:
        anwser = int(input((message)))
    except ValueError:
        return ask_number(message, min_val, max_val)
    else :
        if (isinstance(min_val, int) and anwser < min_val) or (isinstance(max_val, int) and anwser > max_val):
            return ask_number(message, min_val, max_val)
        return anwser

def ask_choice(message: str, options: list) -> int:
    """
    choix = ask_choice("le message en question", ["oui", "non", "jsp"])
    """
    print(message)
    for x in range(len(options)):
        print(f"{x+1}. {options[x]}")
    result = ask_number("Your choice: ", 1, len(options))
    return result


def load_file (file_path: str) -> dict:
    """
    input: file_path
    output: dictionnaire de toute les maisons
    utilisation dictionnaire = load_file("le/chemin/du/fichier.json")
    """
    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)



if __name__ == "__main__":
    choice = ask_number("Courage level (1-10): ", 1, 10)
    choice2 = ask_choice("Do you want to continue ? ", ["Yes", "No"])
    print(load_file("../data/inventory.json"))