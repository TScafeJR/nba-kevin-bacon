from get_all_players import get_all_players
from classes.player import Player

players = get_all_players()
print(players)
# formatted_list = [Player(player_entry) for player_entry in players]
# formatted_player_list = list(map(lambda player_info: Player(player_info),players))
# print(formatted_list)
