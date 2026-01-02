import json, time, threading, sys, time, os

def ask_text(message: str) -> str:
    anwser = ""
    while anwser == "":
        print_slow(message, end="")
        anwser = str(input()).strip()
    return anwser



def ask_number(message: str, min_val=None, max_val=None) -> int:
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
    print_slow(message)
    for x in range(len(options)):
        print(f"{x+1}. {options[x]}")
        time.sleep(0.3)
    result = ask_number("Your choice: ", 1, len(options))
    os.system("cls")
    return result


def load_file(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

def print_slow(*args, vitesse=150, end="\n", flush=False) -> None:
    text = " ".join(str(arg) for arg in args)
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(5/vitesse)
    print(end=end, flush=flush)


def animation_dots(stop_event, custom_message):
    while not stop_event.is_set():
        for dot in ["."*i for i in range(4)]:
            sys.stdout.write(f"\r{custom_message} {dot}   ")
            sys.stdout.flush()
            time.sleep(0.3)
            if stop_event.is_set():
                break

def press_enter_to_continue(custom_message="Press Enter to continue"):
    stop_event = threading.Event()
    animation_thread = threading.Thread(target=animation_dots, args=(stop_event, custom_message))
    animation_thread.daemon = True
    animation_thread.start()
    input()
    stop_event.set()
    animation_thread.join()


if __name__ == "__main__":
    choice = ask_number("Courage level (1-10): ", 1, 10)
    choice2 = ask_choice("Do you want to continue ? ", ["Yes", "No"])
    print(load_file("data/inventory.json"))