import requests
from bs4 import BeautifulSoup


def scraper(url):
    r=requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    keywords=soup.find("meta",attrs={'name':'keywords'})
    print(keywords['content'])
    try:
        return keywords["content"].split(',')
    except:
        return None