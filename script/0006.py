# 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import glob
from 0004 import count_word
def search_dir(dire):
    for fl in glob.glob(os.path.join(dire, '*.txt')):
        counter = count_word(fl)
        counter.sort(key = lambda x: int(x[1]))
        print("%s -> the most word:%s" % (fl, counter[0][0]))
