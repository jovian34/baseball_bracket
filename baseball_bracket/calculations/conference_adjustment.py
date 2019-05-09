power4 = ['SEC', 'Big 12', 'ACC', 'Pac-12', ]
next4 = ['American Athletic', 'Big Ten', 'Missouri Valley', 'West Coast', ]


class ConferenceAdjustment:

    def __init__(self, team_dict):
        self.team_dict = team_dict
        self.adjust_rpi_for_conf_play()

    def adjust_rpi_for_conf_play(self):
        for key, value in self.team_dict.items():
            if value['conf_win_pct'] < 0.5:
                # second lines are midseason adjustments top lines used in May
                self.team_dict[key]['adjusted_rpi'] += -0.015
                # self.team_dict[key]['adjusted_rpi'] += -0.0075
            if value['conf_champs']:
                if value['conference'] in power4:
                    self.team_dict[key]['adjusted_rpi'] += 0.018
                    # self.team_dict[key]['adjusted_rpi'] += 0.009
                elif value['conference'] in next4:
                    self.team_dict[key]['adjusted_rpi'] += 0.013
                else:
                    self.team_dict[key]['adjusted_rpi'] += 0.009

    def return_team_dict(self):
        return self.team_dict
