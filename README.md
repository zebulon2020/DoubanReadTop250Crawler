[中文](README_zh.md)

[English](README.md)

**(a) Crawl Douban Reading Top250 (DoubanSimpleCrawl folder)**

Crawl the page of [Douban Reads Top250](https://book.douban.com/top250?start=0), using BeautifulSoup and pandas.

Time: October 27, 2020

Environment: Python 3.8.3 64 bit

I just learned it, so I solved some problems, but there are also some small bugs.

Problem solved.

+ some books have no synopsis, the csv file will show blank, the synopsis is not misplaced.
+ some books have no translator, it shows normal and no error.

Small bugs:

Show 247, the last 3 did not get saved.

**(II) Top 100 books for data analysis (DoubanReadTop100Statistics folder)**

Crawled the cover images of the top 100 books and analyzed the top 100 books with ratings >=9.5, [9.0, 9.5) and [8.0,9.0), and plotted the fan charts (pie charts).

Time: December 1, 2020

Environment: Python 3.8.3 64 bit

**(III) crawling information and cover, saving to json file, csv file and database, visualization, information query (DoubanAll folder)**

Time: December 21, 2020

Environment: Python 3.8.3 64 bit

+ **crawl.py**: get rank, book title, author, translator, publisher, publication date, price, book link, rating, book description, cover image link, ISBN number
+ **save_json.py**: write book information to book_detail.json file
+ **save_csv.py**: Write book information to BookDouban250.csv file
+ **write_to_mysql.py**: write the book information from the csv file to the MySQL database by line (skip the first line of the csv file)
+ **pic.py**: read the links to the images of each book in the json file, request and download the images based on the links
+ **count_publisher.py**: count publishers, draw bar charts
+ **statist_star.py**: count the intervals in which books are rated, draw a fan chart
+ **search_book.py**: user input, query in database, return results to user.

Note: Use proxy IP in crawl.py file to prevent crawling too often and be blocked IP, maybe the proxy is no longer valid, please modify it by yourself as needed.

-------------------------------------------------
End

Welcome the attention and star
