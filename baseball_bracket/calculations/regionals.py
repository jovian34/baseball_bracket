from baseball_bracket.geography.surrounding import surrounding_map
from pathlib import Path


class Regionals:

    def __init__(self, field, isr_data, team_dict):
        self.field = field
        self.isr_data = isr_data
        self.team_dict = team_dict
        self.regional_dict = {}
        self.create_regional_dict()
        print(self.regional_dict)
        self.matchups = [1, 16, 8, 9, 2, 15, 7, 10, 3, 14, 6, 11, 4, 13, 5, 12]
        self.set_seeds_by_in_state_match(63, 48, -1)  # 4-seeds
        self.set_seeds_by_in_state_match(32, 48)  # 3-seeds
        self.set_seeds_by_in_state_match(31, 16, -1)  # 2-seeds
        self.set_seeds_by_surrounding_state_match(63, 48, -1)  # 4-seeds
        self.set_seeds_by_surrounding_state_match(32, 48)  # 3-seeds
        self.set_seeds_by_surrounding_state_match(31, 16, -1)  # 2-seeds

    @staticmethod
    def calculate_seed(rank):
        if rank < 16:
            return 1
        elif rank < 32:
            return 2
        elif rank < 48:
            return 3
        else:
            return 4

    @staticmethod
    def is_a_host(rank, team):
        if rank < 16:
            return team
        else:
            return None

    def host_already_set(self, team_rank):
        if self.regional_dict[team_rank]['host']:
            return True
        else:
            return False

    def create_regional_dict(self):
        for rank, team in enumerate(self.field):
            self.regional_dict[rank + 1] = {
                'team': team,
                'rank': rank + 1,
                'seed': self.calculate_seed(rank),
                'host': self.is_a_host(rank, team),
                'state': self.isr_data[team]['state'],
                'conference': self.team_dict[team]['conference']
            }

    def set_seeds_by_in_state_match(self, *seed_range):
        for team_rank in range(*seed_range):
            team_conf = self.regional_dict[team_rank]['conference']
            team_state = self.regional_dict[team_rank]['state']
            for host_rank in range(1, 17):
                host_conf = self.regional_dict[host_rank]['conference']
                host_state = self.regional_dict[host_rank]['state']
                if host_conf != team_conf and host_state == team_state:
                    self.regional_dict[team_rank]['host'] = \
                        self.regional_dict[host_rank]['team']
                    break

    def set_seeds_by_surrounding_state_match(self, *seed_range):
        for team_rank in range(*seed_range):
            if self.host_already_set(team_rank):
                continue
            team_conf = self.regional_dict[team_rank]['conference']
            team_state = self.regional_dict[team_rank]['state']
            surr_states = surrounding_map[team_state]
            for host_rank in range(1, 17):
                host_conf = self.regional_dict[host_rank]['conference']
                host_state = self.regional_dict[host_rank]['state']
                if host_conf != team_conf and host_state in surr_states:
                    self.regional_dict[team_rank]['host'] = \
                        self.regional_dict[host_rank]['team']
                    break

    def print_field(self):
        path = Path("2018_regional_dict_v1.txt")
        with open(path, mode='wt') as f:
            f.writelines("Regionals:\n\n")
            for index in self.matchups:
                host = self.regional_dict[index]['team']
                f.writelines(f'Region: {index}\n')
                f.writelines(f"Host: {host} of the "
                             f"{self.team_dict[host]['conference']}\n")
                for two_seed_rank in range(17, 33):
                    two_seed = self.regional_dict[two_seed_rank]
                    if two_seed['host'] == host:
                        f.writelines(f"2-seed: {two_seed['team']} of the "
                                     f"{two_seed['conference']}\n")
                for three_seed_rank in range(33, 49):
                    three_seed = self.regional_dict[three_seed_rank]
                    if three_seed['host'] == host:
                        f.writelines(f"3-seed: {three_seed['team']} of the "
                                     f"{three_seed['conference']}\n")
                for four_seed_rank in range(49, 65):
                    four_seed = self.regional_dict[four_seed_rank]
                    if four_seed['host'] == host:
                        f.writelines(f"4-seed: {four_seed['team']} of the "
                                     f"{four_seed['conference']}\n")
                f.writelines('\n\n')
                f.writelines('\n==============================\n')
