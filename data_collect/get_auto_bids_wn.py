import requests
from bs4 import BeautifulSoup


def request_auto_bid_data(r):
    r_text = r.text
    return BeautifulSoup(r_text, 'html.parser')


def main():
    r = requests.get('http://warrennolan.com/baseball/2018/autobids')
    soup = request_auto_bid_data(r)
    td_text = [td.text.strip() for td in soup.find_all('td') if td.text]
    return td_text


if __name__ == "__main__":
    td_text = main()
    print(td_text)
