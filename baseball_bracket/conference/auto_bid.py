class AutoBid:

    def __init__(self, team_dict, auto_bids):
        self.team_dict = team_dict
        self.auto_bids = auto_bids
        self.set_auto_bids()

    def set_auto_bids(self):
        for key, value in self.auto_bids.items():
            self.team_dict[value]['auto_bid'] = True

    def return_team_dict(self):
        return self.team_dict


