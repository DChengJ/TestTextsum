import sys

from os import listdir
from os.path import isfile, join

dataset_path = "data\\"

def  get_filenames(input_directories):
    dirs = os.listdir(input_directories)
    for file in dirs:
        print(file)
        

#get_filenames(path)
#for f in listdir(dataset_path):
#    print(f)

#onlyfiles = [f for f in listdir(dataset_path) if isfile(join(dataset_path, f))]
#print(onlyfiles)

def read_filenames(dirs_original, dirs_ppt, filenames):
    for filename in filenames:
        article_path = dirs_original + "\\" + filename
        abstract_path = dirs_ppt + "\\" + filename
        with open(article_path) as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
            printlist(content)

def formatcontent(lines, tpyes):
    c = ""
    if types == 'article':
        c = 'article='
    c = "<d> <p>"
    for s in lines:
        c += " <s> %s </s>" % (s)
    c += " </p> </d>" 

def printlist(lists):
    content = "<d> <p>"
    for s in lists:
        content += " <s> %s </s>" % (s)
    content += " </p> </d>"
    print(content)
    print()

def test():
    dataset_path = 'data\\'
    d = '0_Data_Mining_with_Weka'
    dirs_original = dataset_path + d + '\\original'
    dirs_ppt = dataset_path + d + '\\ppt'
    read_filenames(dirs_original, dirs_ppt, ["01_1.txt"])

test()
'''
dirs = []
for d in listdir(dataset_path):
    dirs.append(d)

for d in dirs:
    dirs_original = dataset_path + d + '\\original'
    dirs_ppt = dataset_path + d + '\\ppt'
    filenames = [f for f in listdir(dirs_original) if isfile(join(dirs_original, f))]
    read_filenames(dirs_original, dirs_ppt, filenames)
'''
