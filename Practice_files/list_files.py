from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('/home/gandiv') if isfile(join('/home/gandiv', f))]
print(files_list)
