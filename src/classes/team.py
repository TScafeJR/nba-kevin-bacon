class Team:
    def __init__(self, season_info):
        self.roster = set()
        self.year = season_info.season_year
        self.team_abbr = season_info.team_id
        self.team_id = f'{season_info.team_id}_{season_info.season_year}'

    def add_player(self, player):
        self.roster.add(player.bref_id)