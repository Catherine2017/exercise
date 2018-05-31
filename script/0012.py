import os
import codecs
hexie = set()
with codecs.open('../data/filtered_words.txt', 'r', 'utf-8') as rd:
    lines = rd.readlines()
    hexie = set(map(lambda x: x.rstrip(os.linesep), lines))

string = input("input a string:\n")
for word in hexie:
    if word in string:
        string = string.replace(word, '*'*len(word))
print(string)
