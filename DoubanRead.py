import requests
from bs4 import BeautifulSoup
import pandas

book_name = []  # 书名
book_url = []  # 书籍的豆瓣链接
book_star = []  # 书籍评分
book_author = []  # 书籍作者
book_translater = []  # 书籍译者
book_publisher = []  # 出版社
book_pub_year = []  # 出版日期
book_price = []  # 书籍价格
book_quote = []  # 书籍简介

def get_book_details(url,headers):
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    res = requests.get(url,headers=headers)
    #print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    for book in soup.select('.item'):
        #name = book.select('.pl2 a ')[0].text.strip()
        name = book.select('.pl2 a')[0]['title']    # 书名
        book_name.append(name)
        bkurl = book.select('.pl2 a')[0]['href']  # 书籍链接
        book_url.append(bkurl)
        star = book.select('.rating_nums')[0].text  # 书籍评分
        book_star.append(star)

        ''' 因为有的书籍没有简介，所以有if-else'''
        if(book.select('.quote span')):  
            book_quote.append(book.select('.quote span')[0].text)
        else:
            book_quote.append(None)
        
        info = book.select('.pl')[0].text.split('/')
        #print(info)
        #print(len(info))
        '''有的书籍没有译者，有的书籍有两个价格'''
        if(len(info)==5):
            book_author.append(info[0])
            book_translater.append(info[1])
            book_publisher.append(info[2])
            book_pub_year.append(info[3])
            book_price.append(str(info[4]))
        elif(len(info)==4):
            book_author.append(info[0])
            book_translater.append(None)
            book_publisher.append(info[1])
            book_pub_year.append(info[2])
            book_price.append(str(info[3]))
        elif(len(info)==6):
            book_author.append(info[0])
            book_translater.append(info[1])
            book_publisher.append(info[2])
            book_pub_year.append(info[3])
            book_price.append(str(info[4]) + '/' + str(info[5]))
        else:
            pass
    return


def save_to_csv():
    new_list = []
    new_dict = []
    temp=map(list,zip(book_name,book_author,book_translater,book_publisher,book_pub_year,book_quote,book_price,book_url,book_star))
    for item in temp:
        new_dict = dict(zip(['书名','作者','译者','出版社','出版日期','简介','价格','豆瓣链接','评分'],item))
        new_list.append(new_dict)
    #print(new_list)  
    df = pandas.DataFrame(new_list)
    df.to_csv("BookDouban250.csv")

if __name__ == "__main__":
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    for i in range(10):
        pageUrl = 'https://book.douban.com/top250?start=' + str(i*25)
        get_book_details(pageUrl,headers)
        save_to_csv()
