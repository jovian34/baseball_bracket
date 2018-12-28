from baseball_bracket.conference.auto_bid import AutoBid

class RpiAdjustment:

    def __init__(self):
        self.team_dict = {}
        self.get_data()
        self.adjust_rpi()

    def get_data(self):
        teams = AutoBid()
        self.team_dict = teams.team_dict

    def adjust_rpi(self):
        for key, value in self.team_dict.items():
            if value['conf_win_pct'] <= 0.501:
                self.team_dict[key]['adjusted_rpi'] += -0.015
            if value['conf_champs']:
                self.team_dict[key]['adjusted_rpi'] += 0.018
