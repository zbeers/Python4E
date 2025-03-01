import json
import urllib.request, urllib.parse, urllib.error
import ssl

#Ignores SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2170731.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)
print('User count:', len(info['comments']))
x = 0
nums = list()

for item in info['comments']:
    nums.append(item['count'])

print('Count:', len(nums))
print('Sum:', sum(nums))