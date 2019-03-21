from baseball_bracket.data_collect.req_soup_base import ReqSoup


class BoydsIsr:

    def __init__(self):
        self.req = ReqSoup.make_request('http://www.boydsworld.com/baseball/isr/currentisr.html')
        self.soup = ReqSoup.text_from_request(self.req)
        self.td_text = [td.text.strip() for td in self.soup.find_all('td') if td.text]
        self.remove_header_group()
        self.remove_header_items()
        self.insert_ca_baptist_data()
        self.td_team_lists = []
        self.break_into_sub_lists()
        self.boyd_dict = {}
        self.create_boyd_dict()

    def remove_header_group(self):
        self.td_text = self.td_text[20:-2]

    def remove_header_items(self):
        bad_words = ('Rank', 'Team', 'State', 'Conference', 'Rating', 'W', 'L', 'Sos',
                     '', 'Division I', 'Overall', 'SoS',)
        self.td_text = [item for item in self.td_text if item not in bad_words]

    def insert_ca_baptist_data(self):
        ca_bapt_index = self.td_text.index('California Baptist')
        copy_td_text = self.td_text
        self.td_text = []
        for item in copy_td_text[0:ca_bapt_index + 1]:
            self.td_text.append(item)
        self.td_text.append('CA')
        self.td_text.append('Western Athletic Conference')
        for item in copy_td_text[ca_bapt_index + 1:]:
            self.td_text.append(item)

    def break_into_sub_lists(self):
        self.td_team_lists = [self.td_text[x:x + 10]
                              for x in range(0, len(self.td_text), 10)]

    def create_boyd_dict(self):
        for team_list in self.td_team_lists:
            isr_rank = int(team_list[0])
            team_name = team_list[1].strip().upper()
            state = team_list[2].strip().upper()
            isr = float(team_list[4])

            self.boyd_dict[team_name] = {
                'isr_rank': isr_rank,
                'state': state,
                'isr': isr,
            }

    def get_isr_dict(self):
        return self.boyd_dict






    


