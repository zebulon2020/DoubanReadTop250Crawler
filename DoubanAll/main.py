from crawl import get_res, get_book_details, get_isbn
from save_json import save_to_json
from save_csv import save_to_csv
from write_to_mysql import write_to_mysql
from pic import crawl_image, down_pic
from count_publisher import count_publisher
from statist_star import statist
from search_book import search_book

'''
main函数
'''
if __name__ == "__main__":
    books = []
    for i in range(10):
        pageUrl = 'https://book.douban.com/top250?start=' + str(i*25)
        print("正在爬取"+pageUrl)
        get_book_details(pageUrl, books, i)
        # print(books)
        # print("------------------------------------------------------")
    #print(books)
    for book in books:
        print("正在爬取" + str(book["num"]) + ". 《" +
              book["book_name"] + "》 的ISBN号")
        get_isbn(book["book_url"], book)

    save_to_json(books)
    save_to_csv(books)
    write_to_mysql()
    crawl_image()
    count_publisher()
    statist()
    search_book()
