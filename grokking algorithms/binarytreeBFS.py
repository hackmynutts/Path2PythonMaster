from os import listdir
from os.path import isfile, join
from collections import deque
#
def printname(start_dir):
    search_queue = deque() #Queue to keep track of the folders 
    search_queue.append(start_dir)
    while search_queue: #while queue is not empty pop out a folder to search
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir,file)
            if isfile(fullpath):
                print(file)#if a file print its name
            else:
                search_queue.append(fullpath)#if is a folder added to queue to seach



printname("C:/Users/jorge/OneDrive/Pictures")
