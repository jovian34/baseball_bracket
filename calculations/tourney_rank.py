from calculations.rpi_adjustment import RpiAdjustment
import operator

class TourneyRank:

    def __init__(self):
        self.team_dict = {}
        self.get_data()
        self.team_ranks = []
        self.create_sortable_list()
        self.sort_list()
        self.bumps = 0
        self.qualifiers = []
        self.remove_non_qualifiers()
        self.calculate_bumps()
        self.field_of_64 = []
        self.calc_field_of_64()
        self.print_field()


    def get_data(self):
        teams = RpiAdjustment()
        self.team_dict = teams.team_dict

    def create_sortable_list(self):
        for key, value in self.team_dict.items():
            self.team_ranks.append((key, value['adjusted_rpi'],
                                    value['auto_bid']))

    def sort_list(self):
        self.team_ranks.sort(key=operator.itemgetter(1), reverse=True)

    def remove_non_qualifiers(self):
        self.qualifiers = self.team_ranks[:64]
        for i in range(64, len(self.team_ranks)):
            if self.team_ranks[i][2]:
                self.qualifiers.append(self.team_ranks[i])

    def calculate_bumps(self):
        print(f"{len(self.qualifiers)} initially qualified.")
        self.bumps = len(self.qualifiers) - 64
        print(f"{self.bumps} teams need to be bumped.")

    def calc_field_of_64(self):
        self.qualifiers.sort(key=operator.itemgetter(2, 1), reverse=True)
        self.field_of_64 = self.qualifiers[:64]
        self.field_of_64.sort(key=operator.itemgetter(1), reverse=True)

    def print_field(self):
        for rank, team in enumerate(self.field_of_64):
            print(f"{rank+1}. {team[0]}")
