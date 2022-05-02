import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://en.wikipedia.org/wiki/Outline_of_computer_vision')
soup = BeautifulSoup(res.text, 'html.parser')
h3 = soup.find_all('h3')
subtext = soup.find_all('ul')

cv_sub = []

def create_computer_vision_subsystem():
    for idx, item in enumerate(h3):
        if len(item.select('.mw-headline')):
            sub_topic = []
            for a in item.find_next('ul'):
                if not '\n' in a:
                    sub_topic.append({'name':a.getText(), 'link': a.find_next('a').get('href', None)})
            cv_sub.append({'topic':item.select('.mw-headline')[0].getText(), 'sub_topic':sub_topic})
    return cv_sub

# create_computer_vision_subsystem()
pprint(create_computer_vision_subsystem())

# def create_computer_vision_subsystem():

