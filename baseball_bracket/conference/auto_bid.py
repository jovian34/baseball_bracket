class AutoBid:

    def __init__(self, team_dict, auto_bids):
        self.team_dict = team_dict
        self.auto_bids = auto_bids
        self.set_auto_bids()

    def get_highest_rpi_team_in_conf(self, conference):
        '''
        Prior to auto-bid assignment, this gives the auto
        bid to the team with the highest RPI in the conference
        '''
        highest = [None, 0.0]
        for team, values in self.team_dict.items():
            if values['conference'] == conference:
                if values['rpi'] > highest[1]:
                    highest = [team, values['rpi']]
        return highest[0]

    def set_auto_bids(self):
        for key, value in self.auto_bids.items():
            try:
                self.team_dict[value]['auto_bid'] = True
            except KeyError:
                team = self.get_highest_rpi_team_in_conf(key)
                self.team_dict[team]['auto_bid'] = True

    def return_team_dict(self):
        return self.team_dict


