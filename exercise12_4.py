# coding: utf-8
# Exercise 12.4 Change the urllinks.py program to extract and count paragraph
# (p) tags from the retrieved HTML document and display the count of the para-
# graphs as the output of your program. Do not display the paragraph text, only
# count them. Test your program on several small web pages as well as some larger
# web pages.

import urllib
from bs4 import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

#print soup.prettify().encode('utf-8')

# Retrieve all of the anchor tags
tags = soup('p')
print soup.find_all('p')
#print tags
#count = 0
#for tag in tags:
#    count = count + 1
#print count    