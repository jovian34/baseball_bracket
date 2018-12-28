from baseball_bracket.conference.season_rank import ConferenceRank

class AutoBid:

    def __init__(self):
        self.team_dict = {}
        self.conf_dict = {}
        self.create_dicts()
        self.set_auto_bids()

    def create_dicts(self):
        ranks = ConferenceRank()
        self.team_dict = ranks.team_dict
        self.conf_dict = ranks.conf_dict

    def set_auto_bids(self):
        for key, value in self.conf_dict.items():
            self.team_dict[value]['auto_bid'] = True


