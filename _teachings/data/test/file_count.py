import os

def directory(path,extension): 
    list_dir = [] 
    list_dir = os.listdir(path)
    count = 0 

    for file in list_dir: 
        if file.startswith(extension): # eg: '.txt' 
            count += 1 
    return count

path = './'
extension = 'y2_'

print(directory(path,extension)) 
