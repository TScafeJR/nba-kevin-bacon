class PlayerManager:
    def __init__(self, players):
        self.players = players

    def populate_teammates(self):
        for i, player in enumerate(self.players):
            remaining_player_list = self.players[i:]
            for remaining_player in remaining_player_list:
                if (len(remaining_player.team_id_set & player.team_id_set) > 0):
                    player.add_teammate(remaining_player)
                    remaining_player.add_teammate(player)

        return self.players