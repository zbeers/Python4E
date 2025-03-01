import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignores certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Asks user for url and opens webpage
url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0 #number of comments
total = 0 #total of all comments

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    total += int(tag.contents[0]) #grabs content concatenates and adds it to the total
    count += 1 #increments count

print('Count', count)
print('Sum', total)