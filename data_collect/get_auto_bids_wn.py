from data_collect.req_soup_base import ReqSoup


def break_into_sub_lists(td_text):
    '''
    the Warren Nolan site is not parsing the table correctly
    when using the <tr> tag for rows. So I am taking
    all of the <td> items into a long list.
    Each row produces 4 items so breaking it up every 4
    produces the desired result as of 12/24/2018.
    This could change in the future
    :param data:
    :return:
    '''
    return [td_text[x:x + 4]
            for x in range(0, len(td_text), 4)]


def create_conference_dict(td_list_conf):
    auto_bid_dict = {}
    for conf_list in td_list_conf:
        conf = conf_list[1].strip()
        team = conf_list[3].strip().upper()
        auto_bid_dict[conf] = team
    return auto_bid_dict


def main():
    req = ReqSoup.make_request('http://warrennolan.com/baseball/2018/autobids')
    soup = ReqSoup.text_from_request(req)
    td_text = [td.text.strip() for td in soup.find_all('td') if td.text]
    td_list_conf = break_into_sub_lists(td_text)
    return create_conference_dict(td_list_conf)


if __name__ == "__main__":
    conf_dict = main()
    for key, value in conf_dict.items():
        print(f"{key}: {value}")
