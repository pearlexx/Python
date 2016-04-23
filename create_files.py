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
# C) Create a loop that creates 5 text files of different names

# Courtesy of https://www.youtube.com/watch?v=DRZdfd5_rdg&list=PL82YdDfxhWsC-3kdTKK2_mwbNdBfVvb_M
