import json

def ask_text(message: str) -> str:
    anwser = ""
    while anwser == "":
        anwser = str(input(message+" ")).strip()
    return anwser



def ask_number(message: str, min_val=None, max_val=None) -> int:
    anwser = min_val - 1
    while not (min_val <= anwser <= max_val):
        try:
            anwser = int(input((message)))
        except:
            anwser = min_val - 1





def ask_choice(message: str, options: list) -> int:
    """
    Met sous la forme :
    choix = ask_choice("le message en question", ["oui", "non", "jsp"])
    """
    print(message)
    for x in range(len(options)):
        print(f"{x+1}. {options[x]}")
    result = ask_number(message, 1, len(options))
    return result

def load_file (file_path: str):
    with open(file_path, "r") as json_file:
        return json.load(json_file)



if __name__ == "__main__":
    choice = ask_number("Courage level (1-10): ", 1, 10)
    choice2 = ask_choice("Do you want to continue ? ", ["Yes", "No"])
    print(load_file("../data/inventory.json"))