import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.boydsworld.com/baseball/rpi/currentrpi.html')
r_text = r.text
soup = BeautifulSoup(r_text, 'html.parser')

content = soup.find('pre')

content_str = str(content)
lines = [line for line in content_str.split('\n')]

rpi_dict = {'INDIANA': {'rpi': .500, 'rank': 150, 'wins': 25, 'losses': 25}, }

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
    


