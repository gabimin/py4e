# In order to avoid running out of memory, we retrieve the data in blocks (or buffers) and then write each block to the disk before retrieving the next block
# This way the program can read any size file without using up all of the memory 

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()
