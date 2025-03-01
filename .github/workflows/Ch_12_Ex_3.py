import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#asks user for link, count, and position, then connects to page and sets up soup object
url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))


while count > 0:
    links = list() #creates empty list to index later
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        links.append(tag.get('href', None)) #adds each link to the list
    url = links[pos-1] #makes new url
    print('Retrieving:', url)
    count -=1
