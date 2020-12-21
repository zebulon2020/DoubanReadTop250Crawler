import pymysql
import csv


def write_to_mysql():
    con = pymysql.connect(host='localhost', port=3306, user='root', password='99999999',
                          db='douban_read', cursorclass=pymysql.cursors.DictCursor)
    cursor = con.cursor()
    f = open("BookDouban250.csv", 'r', encoding='utf-8')
    next(f)
    book = []
    for row in csv.reader(f):
        book.append(row)
    f.close()
    sql = "insert into `book250` values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(sql, book)
    con.commit()

    # 关闭连接
    if cursor:
        cursor.close()
    if con:
        con.close()
