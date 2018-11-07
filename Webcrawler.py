from bs4 import BeautifulSoup
from urllib import request
import re

def scrapeLinks(url):
    http  = re.compile('^((http://)|(https://))')
    links = []

    try:
        page = request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser', from_encoding='iso-8859-1')
        
        for tag in soup.find_all('a'):
            link = str(tag.get('href'))
            if http.match(link):
                links.append(link)
    except Exception:
        pass
        
    return(links)

startUrl = 'https://www.netcraft.com/'
visitedLinks = {startUrl}
visitedCount = 1
linkQueue = []

linkQueue = linkQueue + scrapeLinks(startUrl)

#Nb. len() is of O(1) in Python
while visitedCount < 100:
    n = len(linkQueue)
    for link in linkQueue:
        if not link in visitedLinks:
            if visitedCount == 100:
                break
            linkQueue = linkQueue + scrapeLinks(link)
            visitedLinks.add(link)
            visitedCount = len(visitedLinks)
    [linkQueue.pop() for i in range(0,n)]


[print(link) for link in visitedLinks]
