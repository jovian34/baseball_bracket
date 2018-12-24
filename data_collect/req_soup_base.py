import requests
from bs4 import BeautifulSoup

class ReqSoup():

    @staticmethod
    def make_request(url: str)-> object:
        return requests.get(url)


    @staticmethod
    def text_from_request(req):
        req_text = req.text
        return BeautifulSoup(req_text, 'html.parser')

