from random import randint, choice


def create_team(house, team_data, is_player=False, player=None) -> dict:
    result = {
        "name": house, "score": 0, 
        "goals_scored": 0, "goals_blocked": 0, 
        "caught_snitch": False, "players": team_data
        }

    if player and len(team_data) != 0:
        new_list_players = [player + " (Seeker)"]
        for name_player in team_data:
            if name_player not in new_list_players:
                new_list_players.append(name_player)

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


"""
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
