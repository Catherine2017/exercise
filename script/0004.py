#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

import re
from collections import Counter


def count_word(filename):
    words = []
    with open(filename) as rd:
        lines = rd.read()
        lines = re.sub(r'[\!\~\@\#\$\%\^\&\*\(\)\:\;\"\'\?\<\>\.\,\/\\|]+', '',
                       lines)
        reObj = re.compile('\b?(\w+)\b?')
        words = reObj.findall(lines)
    counter = Counter(words)
    return counter

print(count_word('../data/0004.txt').items())
