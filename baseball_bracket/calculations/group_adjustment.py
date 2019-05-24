class GroupAdjustment:

    def __init__(self, team_dict):
        self.team_dict = team_dict
        self.add_group_pcts()

    def add_group_pcts(self):
        for team, values in self.team_dict.items():
            adder = 0
            adder += (values['g1_pct'] - 0.5) * 0.009
            adder += (values['g1_g2_pct'] - 0.5) * 0.0003
            adder += (values['group1_wins']) * 0.0005
            adder += (values['group1_wins']) * 0.0002
            self.team_dict[team]['adjusted_rpi'] += adder

    def return_team_dict(self):
        return self.team_dict

