from bs4 import BeautifulSoup
from urllib import request
import re

def scrapeLinks(url):
    http  = re.compile('^((http://)|(https://))')
    links = []
    
    page = request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    
    for tag in soup.find_all('a'):
        link = str(tag.get('href'))
        if http.match(link):
            links.append(link)
    return(links)

def insertElelment(element, tree, index):
    if element > tree[index][1]:
        if not tree[index][2] == None:
            insertElelment(element, tree, tree[index][2])
        else:
            tree[index] = (tree[index][0], tree[index][1], len(tree))
            tree.append((None,element,None))
    elif element < tree[index][1]:
        if not tree[index][0] == None:
            insertElelment(element, tree, tree[index][0])
        else:
            tree[index] = (len(tree), tree[index][1], tree[index][2])
            tree.append((None,element,None))