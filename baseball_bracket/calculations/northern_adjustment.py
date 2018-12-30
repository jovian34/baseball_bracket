from baseball_bracket.geography.northern_states import northern_states


class NorthernAdjustment:

    def __init__(self, team_data, isr_data):
        self.team_data = team_data
        self.isr_data = isr_data
        self.increase_northern_rpi()

    def increase_northern_rpi(self):
        for team, values in self.isr_data.items():
            if values['state'] in northern_states:
                self.team_data[team]['adjusted_rpi'] += 0.0045

    def return_team_data(self):
        return self.team_data
