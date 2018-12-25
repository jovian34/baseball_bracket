from data_collect.get_current_rpi_wn import NolanRpiExpand
from data_collect.get_auto_bids_wn import NolanAutoBid
from data_collect.get_current_isr_bw import BoydsIsr


class ConferenceRank:

    def __init__(self):
        self.team_dict = {}
        self.conf_dict = {}
        self.conf_win_pct_dict = {}
        self.get_data()
        self.set_conf_win_pct()
        self.conf_high = {key: 0.0 for key in self.conf_dict}
        self.set_best_con_win_pct()
        self.set_conf_champs()


    def get_data(self):
        nolan = NolanRpiExpand()
        nolan_auto = NolanAutoBid()
        boyds_isr = BoydsIsr
        self.conf_dict = nolan_auto.auto_bid_dict
        self.team_dict = nolan.nolan_dict

    def set_conf_win_pct(self):
        for team, t_values in self.team_dict.items():
            for conf in self.conf_dict:
                if t_values['conference'] == conf:
                    wins = float(t_values['conf_wins']) \
                           + (float(t_values['conf_ties']) / 2.0)
                    losses = float(t_values['conf_losses']) \
                             + float((t_values['conf_ties']) / 2.0)
                    win_pct = float(wins / (wins + losses))
                    self.team_dict[team]['conf_win_pct'] = win_pct

    def set_best_con_win_pct(self):
        for team, t_values in self.team_dict.items():
            if t_values['conf_win_pct'] > self.conf_high[t_values['conference']]:
                self.conf_high[t_values['conference']] = t_values['conf_win_pct']

    def set_conf_champs(self):
        for team, t_values in self.team_dict.items():
            if t_values['conf_win_pct'] == self.conf_high[t_values['conference']]:
                self.team_dict[team]['conf_champs'] = True


