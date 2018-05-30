"""第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活
码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import random
import string


def get_coupon(num, length):
    alist = []
    while len(alist) < num:
        strings = ''.join(random.sample(string.ascii_letters + string.digits,
                          length))
        if strings not in alist:
            alist.append(strings)
    return alist


print(get_coupon(200, 20))
