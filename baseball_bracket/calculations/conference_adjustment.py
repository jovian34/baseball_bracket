power4 = ['SEC', 'Big 12', 'ACC', 'Pac-12', ]
next3 = ['American Athletic', 'Big Ten', 'Missouri Valley']
end10 = ['Mountain West', 'West Coast', 'Sun Belt']


class ConferenceAdjustment:

    def __init__(self, team_dict):
        self.team_dict = team_dict
        self.adjust_rpi_for_conf_play()

    def adjust_rpi_for_conf_play(self):
        for key, value in self.team_dict.items():
            if value['conf_win_pct'] < 0.5:
                self.team_dict[key]['adjusted_rpi'] += -0.015
            if value['conf_win_pct'] < 0.45:
                self.team_dict[key]['adjusted_rpi'] += -0.015

            if value['conf_champs']:
                if value['conference'] in power4:
                    self.team_dict[key]['adjusted_rpi'] += 0.018
                elif value['conference'] in next3:
                    self.team_dict[key]['adjusted_rpi'] += 0.012
                elif value['conference'] in end10:
                    self.team_dict[key]['adjusted_rpi'] += 0.009
                else:
                    self.team_dict[key]['adjusted_rpi'] += 0.005

    def return_team_dict(self):
        return self.team_dict
