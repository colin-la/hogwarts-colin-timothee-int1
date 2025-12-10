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



if __name__ == "__main__":
    print(f"launch from {__file__}")
