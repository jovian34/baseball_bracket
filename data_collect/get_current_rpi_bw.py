import requests
from bs4 import BeautifulSoup


def request_rpi_data(r):
    r_text = r.text
    return BeautifulSoup(r_text, 'html.parser')


def get_pre_tag_data(soup):
    content = soup.find('pre')
    content_str = str(content)
    return [line for line in content_str.split('\n')]


def create_rpi_dict(lines, rpi_dict):
    for line in lines:
        try:
            int(line[2])
        except:
            continue
        words = line.split()
        name = line[44:]
        name = name.strip().upper()
        rpi_dict[name] = {
            'rpi': words[1],
            'rank': words[0],
            'wins': words[2],
            'losses': words[3]
        }
    return rpi_dict


def main():
    r = requests.get('http://www.boydsworld.com/baseball/rpi/currentrpi.html')
    soup = request_rpi_data(r)
    lines = get_pre_tag_data(soup)
    rpi_dict = {'INDIANA': {'rpi': .500, 'rank': 150, 'wins': 25, 'losses': 25}, }
    return create_rpi_dict(lines, rpi_dict)


if __name__ == "__main__":
    data = main()
    print(data)
    

