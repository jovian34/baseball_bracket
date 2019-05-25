from baseball_bracket.geography.western_states import western_states


class WesternAdjustment:

    def __init__(self, team_dict, isr_dict):
        self.team_dict = team_dict
        self.isr_dict = isr_dict
        self.rpi_rank_map = self.create_rpi_rank_map()
        self.adjust_rpi_of_western_teams()

    def create_rpi_rank_map(self):
        return {values['rpi_rank']: values['rpi']
                for team, values in self.team_dict.items()}

    def adjust_rpi_of_western_teams(self):
        for team, values in self.isr_dict.items():
            if values['state'] in western_states:
                current_rpi = self.team_dict[team]['rpi']
                isr_rpi = self.rpi_rank_map[values['isr_rank']]
                self.team_dict[team]['adjusted_rpi'] = (((3 * current_rpi) + (2 * isr_rpi)) / 5)


    def return_team_dict(self):
        return self.team_dict
