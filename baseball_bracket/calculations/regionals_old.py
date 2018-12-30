from baseball_bracket.geography.surrounding import surrounding_map
from pathlib import Path


class Regionals:

    def __init__(self, field, isr_data, team_dict):
        self.field = field
        self.isr_data = isr_data
        self.team_dict = team_dict
        self.hosts = self.field[:16]
        print(self.hosts)
        self.non_hosts = [self.field[16:32],
                          self.field[32:48],
                          self.field[48:]]
        print(self.non_hosts)
        self.reverse_even_seeds()
        self.regions = {index+1: {'host': host,
                                  2: None,
                                  3: None,
                                  4: None,
                                  'totals': host[0]}
                        for index, host in enumerate(self.hosts)}
        self.assign_by_same_state()
        self.assign_by_surrounding_state()
        self.assign_remaining()

    def reverse_even_seeds(self):
        self.non_hosts[0].reverse()
        self.non_hosts[2].reverse()

    def assign_by_same_state(self):
        for region, teams in self.regions.items():
            host_state = self.isr_data[teams['host']]['state']
            host_conf = self.team_dict[teams['host']]['conference']
            for seed in (2, 3, 4):
                for team in self.non_hosts[seed - 2]:
                    non_host_conf = self.team_dict[team]['conference']
                    non_host_state = self.isr_data[team]['state']
                    if non_host_state == host_state and host_conf != non_host_conf:
                        self.regions[region][seed] = team
                        self.non_hosts[seed-2].remove(team)
                        continue

    def assign_by_surrounding_state(self):
        for region, teams in self.regions.items():
            host_state = self.isr_data[teams['host']]['state']
            host_conf = self.team_dict[teams['host']]['conference']
            surrounding_states = surrounding_map[host_state]
            for seed in (2, 3, 4):
                if not self.regions[region][seed]:
                    for team in self.non_hosts[seed - 2]:
                        non_host_state = self.isr_data[team]['state']
                        non_host_conf = self.team_dict[team]['conference']
                        if non_host_state in surrounding_states and host_conf != non_host_conf:
                            self.regions[region][seed] = team
                            self.non_hosts[seed - 2].remove(team)
                            continue

    def assign_remaining(self):
        for seed in (2, 3, 4):
            print(f"Remaining {seed}-seeds:")
            for region in self.regions:
                host_conf = self.team_dict[self.regions[region]['host']]['conference']
                if not self.regions[region][seed]:
                    for team in self.non_hosts[seed - 2]:
                        non_host_conf = self.team_dict[team]['conference']
                        if host_conf != non_host_conf:
                            self.regions[region][seed] = team
                            self.non_hosts[seed - 2].remove(team)
                            continue

    def print_field(self):
        path = Path("2018_regionals_v9.txt")
        with open(path, mode='wt') as f:
            f.writelines("Regionals:\n")
            for region, teams in self.regions.items():
                f.writelines(f'Region: {region}\n')
                f.writelines(f"Host: {teams['host']} of the "
                             f"{self.team_dict[teams['host']]['conference']}\n")
                f.writelines(f"2-seed: {teams[2]} \n")
                f.writelines(f"3-seed: {teams[3]} \n")
                f.writelines(f"4-seed: {teams[4]} \n")
                f.writelines('\n\n')
            f.writelines('\n==============================\n')
            for team in self.non_hosts:
                f.writelines(f"Still needing to be placed: {team}\n")
