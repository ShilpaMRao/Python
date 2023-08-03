##
##Extracting Data from XML
##
##In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
##
##We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
##
##Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
##Actual data: http://py4e-data.dr-chuck.net/comments_1853215.xml (Sum ends with 43)


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1: exit

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
commentList = tree.findall(".//comment")


count = 0
sum = 0
for item in commentList:
    count = count + 1
    sum = sum + int(item.find("count").text)

print("Count : ",count)
print("Sum : ",sum)
