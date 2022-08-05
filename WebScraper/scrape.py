import requests
from bs4 import BeautifulSoup
import pprint
# Want to web scrape all stories (title + link) that have > 100 points

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hackernewslist):
    return sorted(hackernewslist, key=lambda k:k['votes'], reverse=True)

# loop through links and votes and only get title and score
def create_custom_hackernews(links, subtext):
    hackernews = []
    for i, link in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hackernews.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hackernews)

pprint.pprint(create_custom_hackernews(links, subtext))