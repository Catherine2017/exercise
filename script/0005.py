# 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import os
from PIL import Image


def thumbnail(scdir, rsdir):
    if not os.path.isdir(rsdir):
        os.makedirs(rsdir)
    for fl in os.listdir(scdir):
        path = os.path.join(scdir, fl)
        try:
            im = Image.open(path)
        except Exception:
            im = None
        if im is not None:
            w, h = im.size
            n = max(w/1366, h/640)
            im.thumbnail(w/n, h/n)
            im.save(os.path.join(rsdir, '{0}.jpg'.format(fl.split('.')[0])), 'jpeg')
    return True
