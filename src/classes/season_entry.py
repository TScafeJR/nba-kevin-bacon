class SeasonEntry:
    def __init__(self, season_info):
        self.season_year = season_info['season']
        self.team_id = season_info['team_id']
        self.league_id = season_info['lg_id']