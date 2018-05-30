# -*- coding: utf-8 -*-
# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
from PIL import Image,ImageFont, ImageDraw
im = Image.open("../data/0000-input.jpg")
font = ImageFont.truetype("arial.ttf", 15)
draw = ImageDraw.Draw(im)
draw.text((160, 0), "20", (255, 0, 0), font=font)
draw = ImageDraw.Draw(im)
im.save("../data/0000-output.jpg")