import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#url = "http://py4e-data.dr-chuck.net/comments_42.html"
url =  "http://py4e-data.dr-chuck.net/comments_1853213.html" 
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


count = 0
total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print(tag)
    print(tag.contents[0])
    count = count +1
    total = total + int(tag.contents[0])
print("Number of values : ",count)
print("Total of the numbers :", total)
    
    
