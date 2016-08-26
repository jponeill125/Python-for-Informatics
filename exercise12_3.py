# coding: utf-8
# Exercise 12.3 Use urllib to replicate the previous exercise of (1) retrieving the
# document from a URL, (2) displaying up to 3000 characters, and (3) counting the
# overall number of characters in the document. Don’t worry about the headers for
# this exercise, simply show the first 3000 characters of the document contents.

import urllib
import string 

# Get users to enter a URL and error check
url = raw_input('Enter a URL: ')
try:
    fhand = urllib.urlopen(url)
    time.sleep(0.5)
except:
        print 'Enter a valid URL of the from http://example.com.'
        exit()
        
#for l in fhand:
#    time.sleep(0.1)
#    line = l.strip()
#    if len(line) <= 0: continue
#    lenght = len(line)
#    print 'Line lenght is', lenght
#    count = count + lenght
#    print 'Total Count is ', count


# Count all characters in webpage. Print the first 3000 chars.
count = 0
str = list()
for l in fhand:
    line = l.strip()
    for letter in line:
        count = count + 1
        if count <= 3000:
           str.append(letter)
text = ''.join(str)
print type(text)
print text
print count