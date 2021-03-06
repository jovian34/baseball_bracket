from baseball_bracket.data_collect.req_soup_base import ReqSoup


class NolanRpiExpand:


    def __init__(self):
        self.req = ReqSoup.make_request('http://warrennolan.com/baseball/2019/rpi-live2')
        self.soup = ReqSoup.text_from_request(self.req)
        self.td_text_delta = [td.text.strip() for td in self.soup.find_all('td') if td.text]
        self.td_text = self.filter_td_text()
        self.remove_rpi_group()
        self.break_into_sub_lists()
        self.nolan_dict = {}
        self.create_nolan_dict()


    def filter_td_text(self):
        '''
        the Warren Nolan site includes a delta number that not all teams have
        that needs to be removed in parsing
        :return: list of strings
        '''
        result = []
        for value in self.td_text_delta:
            if len(value) > 0:
                if value[0] != '+':
                    if value[0] != '-':
                        result.append(value)
        return result



    def remove_rpi_group(self):
        '''
        the Warren Nolan site is not parsing the table correctly
        when using the <tr> tag for rows. So I am taking
        all of the <td> items into a long list.
        The first four items are from a table not
        containing the data we want and needs to be removed.
        :param data: self
        :return: None
        '''
        self.td_text_limited = self.td_text[4:]


    def break_into_sub_lists(self):
        '''
        the Warren Nolan site is not parsing the table correctly
        when using the <tr> tag for rows. So I am taking
        all of the <td> items into a long list.
        Each row produces 18 items so breaking it up every 18
        produces the desired result as of 12/24/2018.
        This could change in the future
        :param data: self
        :return: None
        '''
        self.td_team_lists = [self.td_text_limited[x:x + 17]
                              for x in range(0, len(self.td_text_limited), 17)]

    def create_nolan_dict(self):
        self.nolan_dict = {}
        for team_list in self.td_team_lists:
            rpi_rank = int(team_list[0])

            team_items = team_list[1].split('\n')
            team_name = team_items[0].strip().upper()
            conf_info = team_items[1].split(' (')
            conference = conf_info[0].strip()
            conf_record = conf_info[1].strip(')')
            conf_record = conf_record.split('-')
            conf_wins = int(conf_record[0])
            conf_losses = int(conf_record[1])
            if len(conf_record) == 3:
                conf_ties = int(conf_record[2])
            else:
                conf_ties = 0

            total_record = team_list[2].split('-')
            total_wins = int(total_record[0])
            total_losses = int(total_record[1])
            if len(total_record) == 3:
                total_ties = int(total_record[2])
            else:
                total_ties = 0

            rpi = float(team_list[4])
            sos_rank = int(team_list[5])
            sos = float(team_list[6])

            nc_record = team_list[7].split('-')
            nc_wins = int(nc_record[0])
            nc_losses = int(nc_record[1])
            if len(nc_record) == 3:
                nc_ties = int(nc_record[2])
            else:
                nc_ties = 0

            nc_rpi_rank = int(team_list[8])
            nc_sos_rank = int(team_list[3])

            group1_record = team_list[13].split('-')
            group1_wins = int(group1_record[0])
            group1_lossess = int(group1_record[1])
            group2_record = team_list[14].split('-')
            group2_wins = int(group2_record[0])
            group2_losses = int(group2_record[1])

            g1_games = group1_wins + group1_lossess
            g2_games = group2_wins + group2_losses
            if g1_games == 0:
                g1_pct = .5
            else:
                g1_pct = float(group1_wins / g1_games)
            g1_g2_wins = group1_wins + group2_wins
            g1_g2_games = g1_g2_wins + group1_lossess + group2_losses
            if g1_g2_games == 0:
                g1_g2_pct = .5
            else:
                g1_g2_pct = float(g1_g2_wins / g1_g2_games)

            total_games = total_wins + total_losses + total_ties
            if total_games == 0:
                g1_pct_of_total = 0
                g1_g2_pct_of_total = 0
            else:
                g1_pct_of_total = g1_games / total_games
                g1_g2_pct_of_total = g1_games + g2_games / total_games

            self.nolan_dict[team_name] = {
                'rpi_rank': rpi_rank,
                'conference': conference,
                'conf_wins': conf_wins,
                'conf_losses': conf_losses,
                'conf_ties': conf_ties,
                'conf_win_pct': 0.0,
                'conf_champs': False,
                'auto_bid': False,
                'conf_rpi_lead': False,
                'total_wins': total_wins,
                'total_losses': total_losses,
                'total_ties': total_ties,
                'adjusted_rpi': rpi,
                'rpi': rpi,
                'sos_rank': sos_rank,
                'sos': sos,
                'nc_wins': nc_wins,
                'nc_losses': nc_losses,
                'nc_ties': nc_ties,
                'nc_rpi_rank': nc_rpi_rank,
                'nc_sos_rank': nc_sos_rank,
                'group1_wins': group1_wins,
                'group1_losses': group1_lossess,
                'group2_wins': group2_wins,
                'group2_losses': group2_losses,
                'g1_pct': g1_pct,
                'g1_g2_pct': g1_g2_pct,
                'g1_pct_of_total': g1_pct_of_total,
                'g1_g2_pct_of_total': g1_g2_pct_of_total,
            }

    def get_nolan_dict(self):
        return self.nolan_dict


