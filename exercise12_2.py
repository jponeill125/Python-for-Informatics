# coding: utf-8
# Exercise 12.2 Change your socket program so that it counts the number of char-
# acters it has received and stops displaying any text after it has shown 3000 charac-
# ters. The program should retrieve the entire document and count the total number
# of characters and display the count of the number of characters at the end of the
# document.

#import pdb
#pdb.set_trace()

import socket
import string
str = list()
count = 0


#Get user to enter URL and error check.
url = raw_input('Enter a URL:' )
list = url.split('/')
if len(list) < 2 or list[0] != 'http:':
    print "Enter a valid URL in the form 'http://www.example.com'"
    exit()
else:
    website = list[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((website, 80))
    print 'Success'
except:
    print 'Enter a valid URL'
    exit()

mysock.send('GET http://www.janelwashere.com/files/bible_daily.txt HTTP/1.0\n\n')

#Print the first 3000 characters and count how many characters where recieved.
while True:
    data = mysock.recv(1)
    if ( len(data) < 1 ): 
        break   
    count = count + len(data)
    if count <= 3000:
        str.append(data)
text = ''.join(str)        
print text
print count

mysock.close()