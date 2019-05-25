from baseball_bracket.geography.surrounding import surrounding_map
from pathlib import Path


class Regionals:

    def __init__(self, field, isr_data, team_dict):
        self.field = field
        self.isr_data = isr_data
        self.team_dict = team_dict
        self.regional_dict = {}
        self.create_regional_dict()

        # matchups give the Super Regional pairing orders
        self.matchups = [1, 16, 8, 9, 4, 13, 5, 12, 3, 14, 6, 11, 7, 10, 2, 15]

        self.assign_non_hosts_to_hosts()

    def assign_non_hosts_to_hosts(self):
        self.set_seeds_by_in_state_match(64, 48, -1)  # 4-seeds
        self.set_seeds_by_in_state_match(33, 49)  # 3-seeds
        self.set_seeds_by_in_state_match(32, 16, -1)  # 2-seeds
        self.set_seeds_by_surrounding_state_match(64, 48, -1)  # 4-seeds
        self.set_seeds_by_surrounding_state_match(33, 49)  # 3-seeds
        self.set_seeds_by_surrounding_state_match(32, 16, -1)  # 2-seeds
        self.fill_remaining(64, 48, -1)  # 4-seeds
        self.fill_remaining(33, 49)  # 3-seeds
        self.fill_remaining(32, 16, -1)  # 2-seeds
        self.check_for_empties()


    @staticmethod
    def calculate_seed(rank):
        '''
        for a 64-team fields with 16-regionals
        assigns a 1-4 seed for each rank

        :param rank: integer
        :return: integer
        '''
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
        '''
        returns a team name if the team has a rank
        worthy of a host site

        :param rank: integer
        :param team: string
        :return: string or None
        '''
        if rank < 16:
            return team
        else:
            return None

    def team_already_assigned_host(self, team_rank):
        '''
        A simple dictionary key call and subcall to determine
        if the team has already been assigned to a host

        :param team_rank:
        :return: Boolean
        '''
        if self.regional_dict[team_rank]['host']:
            return True
        else:
            return False

    def host_already_assigned_team(self, host_rank, seed_range):
        '''
        This loops over all 16 teams with the same seed to determine
        if the host already has a team with that seed

        :param host_rank: integer
        :param seed_range: collection of integers
        :return: Boolean
        '''
        host = self.regional_dict[host_rank]['team']
        for i in range(*seed_range):
            if self.regional_dict[i]['host'] == host:
                return True
        return False

    def create_regional_dict(self):
        '''
        This initializes the regional dictionary that is the main
        data container for this class. Only the top-16
        seeds are assigned a host at this point (themselves).

        :return: None
        '''
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
        '''
        this loops over the hosts via the range
        function of host teams, and then the non-hosts
        as determined by the param seed_range
        4-seeds and 2-seeds are set to loop
        backwards in order to assign the lesser
        ranks to the higher ranked hosts
        This function only assigns teams located in
        the same state

        :param seed_range: collection of integers
        :return: None
        '''
        for host_rank in range(1, 17):
            host_team = self.regional_dict[host_rank]['team']
            lower_conf = self.get_lower_conf(host_team)
            host_conf = self.regional_dict[host_rank]['conference']
            host_state = self.regional_dict[host_rank]['state']
            for team_rank in range(*seed_range):
                # print(f"{team_rank} for {seed_range}")
                if self.host_already_assigned_team(host_rank, seed_range):
                    break
                team_conf = self.regional_dict[team_rank]['conference']
                team_state = self.regional_dict[team_rank]['state']
                if self.regional_dict[team_rank]['conference'] in lower_conf:
                    continue
                if host_conf != team_conf and host_state == team_state:
                    self.regional_dict[team_rank]['host'] = \
                        self.regional_dict[host_rank]['team']
                    break

    def get_lower_conf(self, host):
        '''
        Determine what conferences have already been assigned to a host

        :param host: str that is the name of the host assigned
        :return: list of str conferences assigned as 2 through 4 to a host
        '''
        lower_conf = []
        for team in range(17, 65):
            if self.regional_dict[team]['host'] == host:
                lower_conf.append(self.regional_dict[team]['conference'])

        return lower_conf

    def set_seeds_by_surrounding_state_match(self, *seed_range):
        '''
        Mostly the same as set_seeds_by_in_state_match
        but uses surrounding states instead of same states

        :param seed_range: collection of integers
        :return: None
        '''
        for host_rank in range(1, 17):
            host_team = self.regional_dict[host_rank]['team']
            lower_conf = self.get_lower_conf(host_team)
            host_conf = self.regional_dict[host_rank]['conference']
            host_state = self.regional_dict[host_rank]['state']
            for team_rank in range(*seed_range):
                if self.host_already_assigned_team(host_rank, seed_range):
                    break
                if self.team_already_assigned_host(team_rank):
                    continue
                team_conf = self.regional_dict[team_rank]['conference']
                team_state = self.regional_dict[team_rank]['state']
                surr_states = surrounding_map[team_state]
                if self.regional_dict[team_rank]['conference'] in lower_conf:
                    continue
                if host_conf != team_conf and host_state in surr_states:
                    self.regional_dict[team_rank]['host'] = \
                        self.regional_dict[host_rank]['team']
                    break

    def fill_remaining(self, *seed_range):
        '''
        Mostly the same as set_seeds_by_in_state_match
        but no geography test with the goal of assigning all of the
        remaining teams to hosts

        :param seed_range: collection of integers
        :return: None
        '''
        for host_rank in range(1, 17):
            host_team = self.regional_dict[host_rank]['team']
            lower_conf = self.get_lower_conf(host_team)
            host_conf = self.regional_dict[host_rank]['conference']
            for team_rank in range(*seed_range):
                if self.host_already_assigned_team(host_rank, seed_range):
                    break
                if self.team_already_assigned_host(team_rank):
                    continue
                team_conf = self.regional_dict[team_rank]['conference']
                if self.regional_dict[team_rank]['conference'] in lower_conf:
                    continue
                if host_conf != team_conf:
                    self.regional_dict[team_rank]['host'] = \
                        self.regional_dict[host_rank]['team']
                    break

    def check_for_empties(self):
        '''
        This is a print out of teams that couldn't be algorithmically assigned
        with this program and will require manually changing the output txt
        This list should be very small. Hope is to solve this with
        further code in the future

        :return: None
        '''
        for team in range(17, 65):
            if not self.regional_dict[team]['host']:
                print('======NOT ASSIGNED========')
                print(self.regional_dict[team]['team'])
                print(self.regional_dict[team]['conference'])
                print(self.regional_dict[team]['seed'])
                print(self.regional_dict[team]['state'])
                print('======NOT ASSIGNED========')

    def print_field(self):
        '''
        This method writes out a text file that
        describes the field of 64.

        It accesses the hosts via dictionary hash call directly,
        but has to loop over each of the other 3 seeds to find
        its match

        :return: None
        '''
        path = Path("2019_regional_dict_week15-7.txt")
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
