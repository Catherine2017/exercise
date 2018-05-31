# 0007

import re
import os
import glob
import codecs


def line_stat(dire):
    print("files\tall_lines\tspace_lines\texplain_lines")
    for pyfile in glob.glob(os.path.join(dire, '*.py')):
        tot, stot, etot = 0, 0, 0
        with codecs.open(pyfile, 'r', "utf-8") as rd:
            lines = rd.readlines()
            tot = len(lines)
            stot = len(list(filter(lambda x: re.match('^\s*', x), lines)))
            etot = len(list(filter(lambda x: x.startswith('#'), lines)))
        print("{0}\t{1}\t{2}\t{3}".format(pyfile, tot, stot, etot))
    return True

line_stat('./')
