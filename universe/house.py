from math import inf

def update_house_points(houses: dict, house_name: str, points: int) -> None:
    """
    Updates a specific house's points.
    update_house_points({"Gryffindor": 0}, 'Gryffindor', -6) will change the dictionary to {"Gryffindor": -6}
    """
    if house_name not in houses:
        # warning message
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



if __name__ == "__main__":
    print(f"launch from {__file__}")
