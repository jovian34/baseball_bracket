from data_collect.req_soup_base import ReqSoup
from pathlib import Path


class BoydsIsr:


    def __init__(self):
        self.req = ReqSoup.make_request('http://www.boydsworld.com/baseball/isr/currentisr.html')
        self.soup = ReqSoup.text_from_request(self.req)
        self.td_text = [td.text.strip() for td in self.soup.find_all('td') if td.text]
        self.td_text_limited = []
        self.remove_header_group()
        self.td_team_lists = []
        self.break_into_sub_lists()
        self.boyd_dict = {}
        self.create_boyd_dict()
        self.print_isr()

    def remove_header_group(self):

        self.td_text_limited = self.td_text[18:]

    def break_into_sub_lists(self):

        self.td_team_lists = [self.td_text_limited[x:x + 10]
                              for x in range(0, len(self.td_text_limited), 10)]

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

    def print_isr(self):
        path = Path("2018_isr.txt")
        with open(path, mode='wt') as f:
            for key, value in self.boyd_dict.items():
                f.writelines(f"{value['isr_rank']}. {key} ISR: {value['isr']} from {value['state']}")






    


