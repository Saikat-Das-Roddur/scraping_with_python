import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')
links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

mega_subtext = subtext+subtext2
mega_links = links+links2


def sort_stories_by_vote(hnList):
    return sorted(hnList, key= lambda k:k['points'], reverse=True)

def create_custom_hn(links, votes):
    hn = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = votes[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points>99:
                hn.append({'title': title, 'link':href,'points': points})
    return sort_stories_by_vote(hn)

pprint(create_custom_hn(mega_links, mega_subtext))  