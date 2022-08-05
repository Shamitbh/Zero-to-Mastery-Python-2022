import requests
from bs4 import BeautifulSoup

# Want to web scrape all stories (title + link) that have > 100 points

res = requests.get('https://news.ycombinator.com/news')
#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
votes = soup.select('.score')

print(links[0])
print(votes[0])
