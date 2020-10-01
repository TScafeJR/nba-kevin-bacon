class Player:
    def __init__(self, info):
        self.career_start = info['year_min']
        self.career_end = info['year_max']
        self.position = info['pos']
        self.height = info['height']
        self.weight = info['weight']
        self.birth_date = info['birth_date']
        self.colleges = info['colleges']
        self.name = info['player']
        self.bref_id = info['bref_id']
        self.bref_letter = info['bref_letter']
        self.teams = []
        self.teammates = []

    def add_team(self, team):
        self.teams.append(team)

    def add_teammate(self, teammate):
        self.teams.append(teammate)