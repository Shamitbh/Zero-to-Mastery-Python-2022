import requests
from bs4 import BeautifulSoup

# Want to web scrape all stories (title + link) that have > 100 points

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
votes = soup.select('.score')


# loop through links and votes and only get title and score
def create_custom_hackernews(links, votes):
    hackernews = []
    for i, link in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        hackernews.append({'title': title, 'link': href})
    return hackernews

print(create_custom_hackernews(links, votes))