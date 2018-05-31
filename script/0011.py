import os
import codecs
hexie = set()
with codecs.open('../data/filtered_words.txt', 'r', 'utf-8') as rd:
    lines = rd.readlines()
    hexie = set(map(lambda x: x.rstrip(os.linesep), lines))

def get_rt():
    word = input("input a word:\n")
    if word in hexie:
        print("Freedom")
    else:
        print("Human Rights")

get_rt()
