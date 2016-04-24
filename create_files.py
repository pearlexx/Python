import time as t
from os import path


def createFile(dest):
    """
    The script creates a text file at the passed in location
    and names file based on date
    """
    date = t.localtime(t.time())

    # FileName = Month_Day_Year
    name = '%d_%d_%d.txt' % (date[1], date[2], (date[0]%100)) # '%100' takes two last numbers of the year by remainder

    if not(path.isfile(dest + name)):
        f = open(dest + name, 'w')
        f.write('\n'*30)
        f.close()

if __name__ == '__main__':
    destination = 'C:\\Users\\user\\Desktop\\'
    createFile(destination)
    raw_input('done!')

# Tasks
# A) In the script, change the '.txt' extension to something else (html, c, etc.)
# B) Change script to store some text in file


------------------- SOLUTION -------------------
#!/usr/bin/env python

import os.path

path = (os.path.dirname(os.path.realpath(__file__)))

words = "You know what this file could use?"
words += '\nHam'*50

# -- C --
for i in range(5):
	# -- A --
	f = open('%03d_myFile.html'%i, 'w')
	# -- B --
	f.write(words)
	f.close()

print ('done!')
# C) Create a loop that creates 5 text files of different names

# Courtesy of https://www.youtube.com/watch?v=DRZdfd5_rdg&list=PL82YdDfxhWsC-3kdTKK2_mwbNdBfVvb_M
