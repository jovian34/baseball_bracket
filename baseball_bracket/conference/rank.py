class ConferenceRank:

    def __init__(self, team_dict):
        self.team_dict = team_dict
        self.conf_set = self.create_conf_set()
        self.conf_win_pct_dict = {}
        self.set_conf_win_pct()
        self.conf_high = {team: 0.0 for team in self.conf_set}
        self.set_best_conf_win_pct()
        self.conf_rpi_high = {team: 0.0 for team in self.conf_set}
        self.set_conf_leaders()
        self.set_best_conf_rpi()
        self.set_conf_rpi_leaders()
        self.update_team_dict_with_conf_ranks()

    def create_conf_set(self):
        conf_list = [value['conference'] for key, value in self.team_dict.items()]
        return set(conf_list)

    def set_conf_win_pct(self):
        for team, t_values in self.team_dict.items():
            for conf in self.conf_set:
                if t_values['conference'] == conf:
                    wins = float(t_values['conf_wins']) \
                           + (float(t_values['conf_ties']) / 2.0)
                    losses = float(t_values['conf_losses']) \
                             + float((t_values['conf_ties']) / 2.0)
                    try:
                        win_pct = float(wins / (wins + losses))
                    except ZeroDivisionError:
                        win_pct = 0.5
                    self.team_dict[team]['conf_win_pct'] = win_pct

    def set_best_conf_win_pct(self):
        for team, t_values in self.team_dict.items():
            if t_values['conf_win_pct'] > self.conf_high[t_values['conference']]:
                self.conf_high[t_values['conference']] = t_values['conf_win_pct']

    def set_conf_leaders(self):
        for team, t_values in self.team_dict.items():
            if t_values['conf_win_pct'] == self.conf_high[t_values['conference']]:
                self.team_dict[team]['conf_champs'] = True

    def set_best_conf_rpi(self):
        for team, t_values in self.team_dict.items():
            if t_values['rpi'] > self.conf_rpi_high[t_values['conference']]:
                self.conf_rpi_high['conference'] = t_values['rpi']

    def set_conf_rpi_leaders(self):
        for team, t_values in self.team_dict.items():
            if t_values['conf_rpi_lead'] == self.conf_rpi_high[t_values['conference']]:
                self.team_dict[team]['conf_rpi_lead'] = True

    def update_team_dict_with_conf_ranks(self):
        return self.team_dict
