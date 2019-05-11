from baseball_bracket.data_collect.req_soup_base import ReqSoup


class NolanAutoBid:

    def __init__(self):
        self.req = ReqSoup.make_request('http://warrennolan.com/baseball/2019/autobids')
        self.soup = ReqSoup.text_from_request(self.req)
        self.td_text = [td.text.strip() for td in self.soup.find_all('td') if td.text]
        self.td_list_conf = []
        self.break_into_sub_lists()
        self.auto_bid_dict = self.set_auto_bid_dict()
        #self.create_auto_bid_dict()

    def break_into_sub_lists(self):
        """
        the Warren Nolan site is not parsing the table correctly
        when using the <tr> tag for rows. So I am taking
        all of the <td> items into a long list.
        Each row produces 4 items so breaking it up every 4
        produces the desired result as of 12/24/2018.
        This could change in the future
        :param data:
        :return:
        """

        for x in range(0, len(self.td_text), 4):
            self.td_list_conf.append(self.td_text[x:x + 3])

    @staticmethod
    def set_auto_bid_dict():
        return {"ACC": null, "America East": null, "American Athletic": null,
                "Atlantic 10": null, "Atlantic Sun": null, "Big 12": null,
                "Big East": null, "Big South": null, "Big Ten": null,
                "Big West": null, "Colonial Athletic": null,
                "Conference USA": null, "Horizon League": null,
                "Ivy League": null, "MAAC": null, "MEAC": null,
                "Mid-American": null, "Missouri Valley": null,
                "Mountain West": null, "Northeast": null, "Ohio Valley": null,
                "Pac-12": null, "Patriot League": null, "SEC": null,
                "Southern": null, "Southland": null, "Sun Belt": null,
                "SWAC": null, "The Summit League": null, "West Coast": null,
                "Western Athletic": null}

    def create_auto_bid_dict(self):
        for conf_list in self.td_list_conf:
            conf = conf_list[1].strip()
            team = conf_list[3].strip().upper()
            self.auto_bid_dict[conf] = team

    def return_auto_bid_dict(self):
        return self.auto_bid_dict
