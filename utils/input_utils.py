def ask_text(message: str) -> str:
    anwser = ""
    while anwser == "":
        anwser = str(input(message)).strip()
    return anwser

