# 第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
import random
import string
import redis

def get_coupon(num, length):
    alist = []
    while len(alist) < num:
        strings = ''.join(random.sample(string.ascii_letters + string.digits, length))
        if strings not in alist:
            alist.append(strings)
    return alist

def save_code():
    r = redis.Redis(host="127.0.0.1", port='6379', password='linyii')
    codes = get_coupon(200, 20)
    p = r.pipeline()
    for code in codes:
        p.sadd('code', code)
    p.execute()
    return r.scard('code')
