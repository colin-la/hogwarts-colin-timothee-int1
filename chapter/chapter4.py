

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
