def ask_text(message: str) -> str:
    anwser = ""
    while anwser == "":
        anwser = str(input(message+" ")).strip()
    return anwser

question = ask_text("Hello")

def ask_number(message: str, min_val=None, max_val=None) -> int:
    anwser = input(message)
    while True:




def ask_choice(message: str, options):
    pass


def load_file (file_path: str):
    pass