import pymysql
import pandas as pd


def search_book():
    while True:
        print("----------------------------------------------")
        print("从以下选项中任选一项：")
        print("1. 用排名查询\n2. 用书名查询\n3. 查询前x本书籍\n4. 退出")
        choice = int(input("请输入你的选择："))
        if choice == 1:
            number = int(input("请输入你要查询的书籍的排名："))
            con = pymysql.connect(host='localhost', user='root', password='99999999',
                                  db='douban_read', cursorclass=pymysql.cursors.DictCursor)
            try:
                with con.cursor() as cursor:
                    sql = "SELECT * FROM `book250` WHERE `book_ranking`=%s"
                    cursor.execute(sql, (number))
                    result = cursor.fetchone()
                    print(result)
            finally:
                con.close()
        elif choice == 2:
            name = input("请输入你要查询的书名：")
            con = pymysql.connect(host='localhost', user='root', password='99999999',
                                  db='douban_read', cursorclass=pymysql.cursors.DictCursor)
            pattern = '%' + name + '%'
            try:
                with con.cursor() as cursor:
                    sql = "SELECT * FROM `book250` WHERE `book_name` like %s"
                    cursor.execute(sql, (pattern))
                    result = cursor.fetchall()
                    print(result)
            finally:
                con.close()
        elif choice == 3:
            x = int(input("请输入你要查询的前x本书籍中的x："))
            if x <= 0:
                print("输入错误，程序退出！")
                return
            con = pymysql.connect(host='localhost', user='root', password='99999999',
                                  db='douban_read', cursorclass=pymysql.cursors.DictCursor)
            try:
                with con.cursor() as cursor:
                    sql = "SELECT * FROM `book250` WHERE `book_ranking` <= %s"
                    cursor.execute(sql, (x))
                    result = cursor.fetchall()
                    #print(result)
                    df = pd.DataFrame(result)
                    # print(df)
                    df.to_html('x.html', index=False)
                    print("结果已保存在同文件夹下的x.html")
            finally:
                con.close()
        else:
            return
        keep_on = input("是否继续(y / n) ？")
        if keep_on.lower() == 'y':
            pass
        else:
            return
        # return
