import collections
import sys
import os
import re
from os import listdir
from os.path import isfile, join

dataset_path = "data\\"
artucle_name = "transcript"
abstract_name = "ppt"
article_path = ""
abstract_path = ""
vocabulary_filename = "vocab"
output_filename = "text_data"

def ensure_dir(dir_path):
    directory = os.path.dirname(dir_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def files_to_vocab(dataset_path, vocabulary_filename, max_words=200000):
    dirs = get_lessons(input_directories)
    #ensure_dir('.\\vocabs\\')
    #filenames = ['data\\0_Data_Mining_with_Weka\\original\\01_1.txt','data\\0_Data_Mining_with_Weka\\original\\02_2.txt']
    filenames = []
    counter = collections.Counter()
    
    for d in dirs:
        article_path = dataset_path + d + "\\" + artucle_name + "\\"
        fs = [f for f in listdir(article_path) if isfile(join(article_path, f))]
        for f in fs:
            filenames.append(article_path + f)
    
    document_num = 0
    lines = 0
    for filename in filenames:
        document_num += 1
        with open(filename, 'r') as f:
            for line in f:
                lines += 1
        with open(filename, 'r') as f:
            document = f.read()
            #print(document)
        words = re.findall(r"[\w]+|[^\s\w]", document)
        words = map(lambda x:x.lower(), words)
        counter.update(words)
    
    with open(vocabulary_filename, 'w') as writer:
        for word, count in counter.most_common(max_words - 2):
            writer.write(word + ' ' + str(count) + '\n')
        writer.write('<s> ' + str(lines) + '\n')
        writer.write('</s> ' + str(lines) + '\n')
        writer.write('<d> ' + str(document_num) + '\n')
        writer.write('</d> ' + str(document_num) + '\n')
        writer.write('<UNK> 0\n')
        writer.write('<PAD> 5\n')
        
def file_to_text(dataset_path, output_filename):
    dirs = get_lessons(dataset_path)
    '''
    filenames = ['01_1.txt','02_2.txt']
    d = "0_Data_Mining_with_Weka"
    with open(output_filename, 'w') as writer:
        for filename in filenames:
            article_path = dataset_path + d + "\\" + artucle_name + "\\" + filename
            abstract_path = dataset_path + d + "\\" + abstract_name + "\\" + filename
            writer.write("abstract=b'%s'\tartucle=b'%s'\tpublisher=b'%s'\n" % (formatcontent(abstract_path), formatcontent(article_path), d))
            #print("abstract=b'%s'\tartucle=b'%s'\tpublisher=b'%s'\n" % (formatcontent(abstract_path), formatcontent(article_path), d))
    '''
    for d in dirs:
        article_path = dataset_path + d + "\\" + artucle_name + "\\"
        abstract_path = dataset_path + d + "\\" + abstract_name + "\\"
        filenames = [filename for filename in listdir(article_path) if isfile(join(article_path, filename))]
        with open(output_filename, 'w', encoding='utf8') as writer:
            for f in filenames:
                article_path = dataset_path + d + "\\" + artucle_name + "\\" + f
                abstract_path = dataset_path + d + "\\" + abstract_name + "\\" + f
                writer.write("abstract=b'%s'\tartucle=b'%s'\tpublisher=b'%s'\n" % (formatcontent(abstract_path), formatcontent(article_path), d))
                #print("abstract=b'%s'\tartucle=b'%s'\tpublisher=b'%s'\n" % (formatcontent(abstract_path), formatcontent(article_path), d))

def formatcontent(path):
    print(path)
    content = "<d> <p>"
    with open(path, 'r', encoding='utf8') as f:
        for line in f:
            line = line.strip()
            content += " <s> %s </s>" % (line)
        '''
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        for s in lines:
            content += " <s> %s </s>" % (s)
        '''
        content += " </p> </d>"
    return content

def get_lessons(dataset_path):
    dirs = []
    for d in listdir(dataset_path):
        dirs.append(d)
    return dirs

file_to_text(dataset_path, output_filename)
#files_to_vocab(dataset_path, vocabulary_filename)
