[English](./README.md)

[中文](README_zh.md)

**（一）爬取豆瓣读书 TOP250  （DoubanSimpleCrawl 文件夹）**

爬取[豆瓣读书 Top250](https://book.douban.com/top250?start=0) 的页面,运用了 BeautifulSoup 和 pandas。

时间：2020 年 10 月 27 日

环境：Python 3.8.3 64bit

因为刚刚学习，所以解决了一些问题，但也有一些小 bug。

解决的问题：

+ 有的书籍没有简介，csv 文件中会显示空白，简介并没有错位；
+ 一些书籍没有译者，显示正常，没有错误；

小 bug:

显示 247 个，最后 3 个没有得到保存。

**(二)数据分析前 100 本书（DoubanReadTop100Statistics 文件夹）**

爬取了前 100 本书的封面图片，并分析了前 100 本书评分 >=9.5 的，[9.0, 9.5)的和[8.0,9.0)的情况，绘制了扇形图（饼状图）。

时间：2020 年 12 月 1 日

环境：Python 3.8.3 64bit

**(三)爬取信息和封面、保存到 json 文件、csv 文件和数据库、可视化、信息查询（DoubanAll 文件夹）**

时间：2020 年 12 月 21 日

环境：Python 3.8.3 64bit

+ **crawl.py**: 获取排名、书名、作者、译者、出版社、出版日期、价格、书籍链接、评分、书籍简介、封面图片链接、ISBN 号
+ **save_json.py**: 把书籍信息写入 book_detail.json 文件中
+ **save_csv.py**: 把书籍信息写入 BookDouban250.csv 文件中
+ **write_to_mysql.py**: 把 csv 文件中书籍的信息按行写入 MySQL 数据库（跳过 csv 文件第一行）
+ **pic.py**: 读取 json 文件中每本书的图片链接，根据链接请求和下载图片
+ **count_publisher.py**: 统计出版社，绘制柱状图
+ **statist_star.py**: 统计书籍评分所在区间，绘制扇形图
+ **search_book.py**: 用户输入，在数据库中查询，返回结果给用户。

注意：在 crawl.py 文件中使用了代理 IP 防止爬取过于频繁而被封禁 IP，可能代理已失效，请自行按需修改。

---

End

欢迎关注和 star
