import operator
from pathlib import Path


class TourneyRank:

    def __init__(self, team_dict):
        self.team_dict = team_dict
        self.team_ranks = []
        self.create_sortable_list()
        self.sort_list()
        self.bumps = 0
        self.qualifiers = []
        self.remove_non_qualifiers()
        self.calculate_bumps()
        self.field_of_64 = []
        self.last_four_in = []
        self.first_four_out = []
        self.calc_field_of_64()
        self.field_of_64 = self.create_field_name_list()

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
        self.last_four_in = self.qualifiers[60:64]
        self.first_four_out = self.qualifiers[64:68]
        self.last_four_in.reverse()
        self.field_of_64.sort(key=operator.itemgetter(1), reverse=True)

    def create_field_name_list(self):
        return [team[0] for team in self.field_of_64]

    def return_field(self):
        return self.field_of_64

    def print_field(self):
        path = Path("2019_ranks_14-2.txt")
        with open(path, mode='wt') as f:
            f.writelines("Last Four in:\n")
            for rank, team in enumerate(self.last_four_in):
                f.writelines(f"{rank+1}. {team[0]}\n")
            f.writelines("\n\n")

            f.writelines("First Four out:\n")
            for rank, team in enumerate(self.first_four_out):
                f.writelines(f"{rank + 1}. {team[0]}\n")
            f.writelines("\n\n")

            f.writelines("Ranked Field of 64:\n")
            for rank, team in enumerate(self.field_of_64):
                f.writelines(f"{rank+1}. {team}\n")
