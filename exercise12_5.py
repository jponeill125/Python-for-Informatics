# coding: utf-8
# Exercise 12.5 (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember that recv is
# receiving characters (newlines and all), not lines.


#import pdb
#pdb.set_trace()

import socket
import string
import time
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
    data = mysock.recv(2)
    if ( len(data) < 1 ): 
        break   
    count = count + len(data)
    if data == ' \n\n':
        print data
        print 'Hello'
    
    
    
    
#    if count <= 3000:
#        print data
        time.sleep(0.2)
#        str.append(data)
#text = ''.join(str)        
#print text
#print count

mysock.close()