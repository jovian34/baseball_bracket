from data_collect.req_soup_base import ReqSoup


class BoydsRpi:


    def __init__(self):
        self.req = ReqSoup.make_request('http://www.boydsworld.com/baseball/rpi/currentrpi.html')
        self.soup = ReqSoup.text_from_request(self.req)
        self.lines = []
        self.get_pre_tag_data()
        self.rpi_dict = {'INDIANA': {'rpi': .500, 'rank': 150, 'wins': 25, 'losses': 25}, }
        self.nolan_rpi_dict = {}
        self.populate_rpi_dict()


    def get_pre_tag_data(self):
        content = self.soup.find('pre')
        content_str = str(content)
        self.lines = [line for line in content_str.split('\n')]


    def populate_rpi_dict(self):
        for line in self.lines:
            try:
                int(line[2])
            except:
                continue
            words = line.split()
            name = line[44:]
            name = name.strip().upper()
            self.nolan_rpi_dict[name] = {
                'rpi': float(words[1]),
                'rank': int(words[0]),
                'wins': int(words[2]),
                'losses': int(words[3]),
            }





    


