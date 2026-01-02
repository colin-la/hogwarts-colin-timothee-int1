from math import inf
from utils.input_utils import *

def update_house_points(houses: dict, house_name: str, points: int) -> None:
    if house_name not in houses:
        print("WARNING: The house's name you're trying to update is NOT in the dictionary provided.")
        return
    houses[house_name] += points
    if points < 0:
        context = "lost"
    else:
        context = "gained"
    print("The house {} has {} {} point(s)!".format(house_name, context, points))
    print("It now has {} point(s).".format(houses[house_name]))

def display_winning_house(houses: dict) -> None:
    maxi = -1 * inf
    for points in houses.values():
        if maxi < points:
            maxi = points
    print("Here are the winning house(s):\n")
    for house, points in houses.items():
        if points == maxi:
            print("- {} with {} point(s)!".format(house, points))

def assign_house(character: dict, questions: list) -> str:
    dico = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}
    for attribute, value in character["Attributes"].items():
        if attribute == 'Courage':
            name = "Gryffindor"
        elif attribute == 'Ambition':
            name = "Slytherin"
        elif attribute == "Loyalty":
            name = "Hufflepuff"
        else:
            name = "Ravenclaw"
        dico[name] += value * 2

    for question, answer_list, house_list in questions:
        choice = ask_choice(question, answer_list)
        dico[house_list[choice-1]] += 3
        print()

    print("Summary of scores:")
    for house, points in dico.items():
        print("{}: {} points".format(house, points))
    maxi = -1 * inf
    for points in dico.values():
        if maxi < points:
            maxi = points
    for house, points in dico.items():
        if points == maxi:
            return house



if __name__ == "__main__":
    print(f"launch from {__file__}")
