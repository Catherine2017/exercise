# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import random
import string
import mysql.connector

def get_coupon(num, length):
    alist = []
    while len(alist) < num:
        strings = ''.join(random.sample(string.ascii_letters + string.digits, length))
        if strings not in alist:
            alist.append(strings)
    return alist

def save_code():
    conn = mysql.connector.connect(user="root", password="1", database="test")
    cursor = conn.cursor()
    codes = get_coupon(200, 20)
    for code in codes:
        cursor.execute("INSERT INF `code`(`code`) VALUES(%s)", params=[code])
    conn.commit()
    cursor.close()
