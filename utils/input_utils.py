import json, time, threading, sys, time

def ask_text(message: str) -> str:
    """
    texte = ask_text("le message en question")
    """
    anwser = ""
    while anwser == "":
        print_slow(message, end="")
        anwser = str(input()).strip()
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
        print("Error, please enter a numerical value.")
        return ask_number(message, min_val, max_val)
    else :
        if (isinstance(min_val, int) and anwser < min_val) or (isinstance(max_val, int) and anwser > max_val):
            print("Error, the number isn't in the available choices.")
            return ask_number(message, min_val, max_val)
        return anwser

def ask_choice(message: str, options: list) -> int:
    """
    choix = ask_choice("le message en question", ["oui", "non", "jsp"])
    choix takes 1, 2 or 3
    """
    print_slow(message)
    for x in range(len(options)):
        print(f"{x+1}. {options[x]}")
        time.sleep(0.3)
    result = ask_number("Your choice: ", 1, len(options))
    return result


def load_file(file_path: str) -> dict:
    """
    input: file_path
    output: dictionnaire de toute les maisons
    utilisation dictionnaire = load_file("le/chemin/du/fichier.json")
    """
    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

def print_slow(*args, vitesse=150, end="\n", flush=False) -> None:
    """
    comme un print mais avec une vitesse variable 
    le caractere retour à la ligne est supportés
    vitesse par défaut = 100
    vitesse très lente = 40
    vitesse normal = 100
    vitesse très rapide = 300
    """
    # This line helps to take differents parameters like the real print()
    text = " ".join(str(arg) for arg in args)
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(5/vitesse)
    print(end=end, flush=flush)


if __name__ == "__main__":
    choice = ask_number("Courage level (1-10): ", 1, 10)
    choice2 = ask_choice("Do you want to continue ? ", ["Yes", "No"])
    print(load_file("./data/inventory.json"))