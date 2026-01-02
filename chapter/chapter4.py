from random import randint, choice
from utils.input_utils import *
from universe.house import *
from universe.character import *

def create_team(house: str, team_data: dict, is_player=False, player=None) -> dict:
    result = {
        "name": house, "score": 0, 
        "goals_scored": 0, "goals_blocked": 0, 
        "caught_snitch": False, "players": []
        }

    new_list_players = []
    for name_player in team_data:
        if "(Seeker)" in name_player and is_player : 
            name_player = f"{player} (Seeker)"
        new_list_players.append(name_player)
    result["players"] = new_list_players
    return result


def attempt_goal(attacking_team, defending_team, player_is_seeker=False) -> None:
    print_slow(f"The attacking team is attempting to score a goal !")
    print_slow(f" - Attaaaaack ! says the team leader !")
    chance_goal = randint(1, 10)
    if chance_goal >= 6:
        if player_is_seeker:
            scoring_player = attacking_team["players"][0]
        else :
            scoring_player = choice(attacking_team["players"][1::])
        attacking_team["score"] += 10
        attacking_team["goals_scored"] += 1
        print_slow(f"This attack was amazing ! {scoring_player} scores a goal for {attacking_team["name"]} ! (+10 points)\n")
    else :
        defending_team["goals_blocked"] += 1
        print_slow(f"The attack wasn't strong enough ! {defending_team["name"]} blocked the attack!\n")

def golden_snitch_appears() -> bool:
    return randint(1, 6) == 6

def catch_golden_snitch(e1: dict, e2: dict) -> dict:
    winner = choice([e1, e2])
    winner["score"] += 150
    winner["caught_snitch"] = True 
    return winner

def display_score(e1: dict, e2: dict) -> None:
    print("Current score:\n")
    print("-> {}: {} points".format(e1['name'], e1['score']))
    print("-> {}: {} points".format(e2['name'], e2['score']))


def display_team(house: str, team: list) -> None:
    print("{} team:\n".format(house))
    for member in team:
        print('-', member)

def quidditch_match(character, houses):
    data = load_file("data/teams_quidditch.json")
    opponent_house = player_house = character["House"]
    while opponent_house == player_house:
        opponent_house = choice(list(data.keys()))
    player_team = create_team(house=player_house, 
                            team_data=data[player_house]["players"], is_player=True, 
                            player=character["First Name"] + " " + character["Last Name"])
    opponent_team = create_team(house=opponent_house, 
                            team_data=data[opponent_house]["players"], is_player=False)
    display_team(player_house, player_team["players"])
    display_team(opponent_house, opponent_team["players"])
    print_slow(f"You are playing for {player_team["name"]} as the Seeker\n")
    for i in range(20):
        print(f"━━━ Round {i+1} ━━━")
        attempt_goal(attacking_team=player_team, defending_team=opponent_team, player_is_seeker=True)
        attempt_goal(defending_team=player_team, attacking_team=opponent_team, player_is_seeker=False)
        display_score(e1=player_team, e2=opponent_team)
        if golden_snitch_appears():
            winning_house = catch_golden_snitch(player_team, opponent_team)["name"] 
            print_slow(f"The Golden Snitch has been caught by {winning_house} ! (+150 points)\n")
            print_slow("End of the match !\n")
            break
        input("Press Enter to start the next round ...")
    display_score(e1=player_team, e2=opponent_team)
    if player_team["score"] > opponent_team["score"]:
        winning_house = player_house
    elif player_team["score"] == opponent_team["score"]:
        winning_house = None
    else :
        winning_house = opponent_house
    if winning_house != None:
        update_house_points(houses, winning_house, 500)
    

def start_chapter_4_quidditch(character, houses):
    print_slow("Welcome to the Chapter 4.")
    print_slow("Today, you will participate in a Quidditch match.")
    print_slow("Are you ready ? Let's goooooo !!!\n")
    quidditch_match(character, houses)
    print_slow("End of Chapter 4 — What an incredible performance on the field!\n")
    display_winning_house(houses)
    display_character(character)
    




if __name__ == "__main__":
    print(f"launch from {__file__}")
