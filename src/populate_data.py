from get_all_players import get_all_players
from get_all_teams import add_team_and_season_info_to_player
from classes.player_manager import PlayerManager
import json
import jsonpickle

#add all players
players = get_all_players()

# add season info and team info to each player in list
players_with_season_info = list(map(lambda player: add_team_and_season_info_to_player(player), players))

# instantiate player manager class
playerManager = PlayerManager(players_with_season_info)

# print(json.dumps(playerManager.populate_teammates(), indent=4))
print(jsonpickle.encode(playerManager.populate_teammates()))