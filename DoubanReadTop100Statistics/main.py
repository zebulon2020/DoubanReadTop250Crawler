import json
import requests
from bs4 import BeautifulSoup
import os

from statistics import statist   # 同文件夹自己写的statistics.py

books = []

def crawl_data(headers, url):
    '''
    爬取豆瓣读书top250的前100本书籍，并把每本书籍的信息写入json文件
    '''
    try:
        print(url)
        res = requests.get(url, headers=headers)
        #print(res.text)
        soup = BeautifulSoup(res.text, 'html.parser')
        for aBook in soup.select('.item'):
            book = {}
            book["name"] = aBook.select('.pl2 a')[0]['title']    # 书名
            book["url"] = aBook.select('.pl2 a')[0]['href']  # 书籍链接
            book["rating_num"] = aBook.select('.rating_nums')[0].text  # 书籍评分
            ''' 因为有的书籍没有简介，所以有if-else'''
            if(aBook.select('.quote span')):  
                book["quote"] = aBook.select('.quote span')[0].text  # 书籍简介
            else:
                book["quote"] = "None"
            
            info = aBook.select('.pl')[0].text.split('/')

            '''有的书籍没有译者，有的书籍有两个价格'''
            if(len(info)==5):
                book["author"] = info[0]  # 书籍作者
                book["translater"] = info[1]  # 书籍译者
                book["publisher"] = info[2]  # 书籍出版社
                book["pub_year"] = info[3]  # 书籍出版日期
                book["price"] = str(info[4])  # 书籍价格
            elif(len(info)==4):
                book["author"] = info[0]
                book["translater"] = "None"
                book["publisher"] = info[1]
                book["pub_year"] = info[2]
                book["price"] = str(info[3])
            elif(len(info)==6):
                book["author"] =info[0]
                book["translater"] = info[1]
                book["publisher"] = info[2]
                book["pub_year"] = info[3]
                book["price"] = str(info[4]) + '/' + str(info[5])
            else:
                pass

            book["pic_url"] = aBook.select('.nbg img')[0].get('src')  # 书籍图片链接
            #print(book)
            books.append(book)
            #print(books)
        json_data = json.loads(str(books).replace("'", "\""))
        with open('book_detail.json', 'w', encoding='UTF-8') as f:
            json.dump(json_data, f, ensure_ascii=False)
    except Exception as e:
        print(e)

def crawl_image():
    '''
    爬取书籍的图片的url，调用down_pic函数下载图片
    '''
    with open('book_detail.json', 'r', encoding='UTF-8') as file:
        json_array = json.loads(file.read())
    
    for book in json_array:
        name = book['name']
        pic_link = book['pic_url']
        down_pic(name, pic_link)

def down_pic(name, pic_url):
    '''
    根据图片url下载书籍图片，保存在以name命名的文件夹
    '''
    print(pic_url)
    path = 'data/' + 'pics/' + name + '/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    try:
        pic = requests.get(pic_url, timeout=15)
        string = name + '.jpg'
        with open(path+string, 'wb') as f:
            f.write(pic.content)
            print('成功下载' + name + '图片')
    except Exception as e:
        print('下载'+ name + '图片失败')
        print(e)

if __name__ == "__main__":
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    for i in range(4):
        pageUrl = 'https://book.douban.com/top250?start=' + str(i*25)
        crawl_data(headers, pageUrl)
    crawl_image()
    statist()
    