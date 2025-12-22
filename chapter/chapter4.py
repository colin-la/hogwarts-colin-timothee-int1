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
    print(f"The attacking team is attempting to score a goal !")
    print(f" - Attaaaaack ! says the team leader !")
    chance_goal = randint(1, 10)
    if chance_goal >= 6:
        if player_is_seeker:
            scoring_player = attacking_team["players"][0]
        else :
            scoring_player = choice(attacking_team["players"][1::])
        attacking_team["score"] += 10
        attacking_team["goals_scored"] += 1
        print(f"This attack was amazing ! {scoring_player} scores a goal for {attacking_team["name"]} ! (+10 points)")
    else :
        defending_team["goals_blocked"] += 1
        print(f"The attack wasn't strong enough ! {defending_team["name"]} blocked the attack!")

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
    print(f"You are playing for {player_team["name"]} as the Seeker")
    for i in range(20):
        print(f"━━━ Turn {i+1} ━━━")
        attempt_goal(attacking_team=player_team, defending_team=opponent_team, player_is_seeker=True)
        attempt_goal(defending_team=player_team, attacking_team=opponent_team, player_is_seeker=False)
        display_score(e1=player_team, e2=opponent_team)
        if golden_snitch_appears():
            winning_house = catch_golden_snitch(player_team, opponent_team)["name"] 
            print(f"The Golden Snitch has been caught by {winning_house} ! (+150 points)")
            print("End of the match !")
            break
        input("Press Enter to start the next round ...")
    display_score(e1=player_team, e2=opponent_team)
    if player_team["score"] > opponent_team["score"]:
        winning_team = player_house
    elif player_team["score"] == opponent_team["score"]:
        winning_team = None # nobody wins
    else :
        winning_team = opponent_house
    if winning_team != None:
        # update_house_points(houses[winning_house], winning_house, 500)
        # TO FIX
        pass 
    

def start_chapter_4_quidditch(character, houses):
    print("Welcome to the Chapter 4.")
    print("Today, you will participate in a Quidditch match.")
    print("Are you ready ? Let's goooooo !!!")
    quidditch_match(character, houses)
    print("End of Chapter 4 — What an incredible performance on the field!")
    display_winning_house(houses)
    display_character(character)
    


"""
character = {'Last Name': 'qsdf', 
'First Name': 'qdfsqsf', 'Money': 100, 
'Inventory': [], 'Spells': [], 
'Attributes': {'Courage': 1, 'Intelligence': 1, 
                'Loyalty': 1, 'Ambition': 1}}
team = {
'name': 'Gryffindor',
'score': 0,
'has_scored': 0,
'has_stopped': 0,
'caught_snitch': False,
'players': [
'Harry Potter (Seeker)',
'Ginny Weasley (Chaser)',
'Katie Bell (Chaser)',
'Demelza Robins (Chaser)',
'Ron Weasley (Keeper)',
'Jimmy Peakes (Beater)',
'Ritchie Coote (Beater)']}
"""

if __name__ == "__main__":
    print(f"launch from {__file__}")
