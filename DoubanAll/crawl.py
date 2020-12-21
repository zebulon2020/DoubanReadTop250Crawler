import requests
from bs4 import BeautifulSoup
import re


def get_res(url):
    try:
        proxies = {
            # 'http':'http://112.17.14.39:8080',
            # 'http':'http://112.17.14.27:8080',
            # 'http':'http://115.236.100.104:8080',
            # 'http':'http://115.216.1.253:1080',
            'http': 'http://218.75.70.3:1080',
            # 'http':'http://120.26.66.53:1080',
            # 'http':'http://121.199.1.198:8080',
            # 'http':'http://183.129.178.9:1080',
            # 'http':'http://121.52.241.203:1080',
            # 'http':'http://60.177.228.4:1080',
            # 'http':'http://183.247.152.98:53281',
            # 'http':'http://125.122.148.44:9000',
            # 'http':'http://183.159.87.206:1080',
            # 'http':'http://125.118.150.44:1080',
            # 'http':'http://58.101.16.133:8888',
            # 'http':'http://220.191.102.154:1080',
            # 'http':'http://125.118.72.241:1080',
            # 'http':'http://121.199.38.96:8081',
        }
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        res = requests.get(url, headers=head, proxies=proxies)
        res.raise_for_status()
        return res
    except:
        return "Get response Error"


def get_book_details(url, books, page):
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    res = get_res(url)
    #print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    count = 0
    for abook in soup.select('.item'):
        count = count + 1
        book = {}
        book["num"] = count + 25*page
        #name = book.select('.pl2 a ')[0].text.strip()
        name = abook.select('.pl2 a')[0]['title']    # 书名
        book["book_name"] = name
        #print(name)

        info = abook.select('.pl')[0].text.split('/')
        #print(info)
        #print(len(info))
        '''有的书籍没有译者，有的书籍有两个价格'''
        if(len(info) == 5):
            book["book_author"] = info[0]
            book["book_translater"] = info[1]
            book["book_publisher"] = info[2]
            book["book_pub_year"] = info[3]
            book["book_price"] = str(info[4])
        elif(len(info) == 4):
            book["book_author"] = info[0]
            book["book_translater"] = None
            book["book_publisher"] = info[1]
            book["book_pub_year"] = info[2]
            book["book_price"] = str(info[3])
        elif(len(info) == 6):
            book["book_author"] = info[0]
            book["book_translater"] = info[1]
            book["book_publisher"] = info[2]
            book["book_pub_year"] = info[3]
            book["book_price"] = str(info[4]) + '/' + str(info[5])
        elif(len(info) == 3):
            book["book_author"] = None
            book["book_translater"] = None
            book["book_publisher"] = info[0]
            book["book_pub_year"] = info[1]
            book["book_price"] = info[2]
        else:
            pass

        bkurl = abook.select('.pl2 a')[0]['href']  # 书籍链接
        book["book_url"] = bkurl

        star = abook.select('.rating_nums')[0].text  # 书籍评分
        book["book_star"] = star

        ''' 因为有的书籍没有简介，所以有if-else'''
        if(abook.select('.quote span')):
            book["book_quote"] = abook.select('.quote span')[0].text  # 书籍简介
        else:
            book["book_quote"] = None

        book["pic_url"] = abook.select('.nbg img')[0].get('src')  # 书籍图片链接
        books.append(book)
    return


def get_isbn(bkurl, book):
    '''
    获取书籍的ISBN号
    '''
    res2 = get_res(bkurl)
    pattern = r'<span class="pl">ISBN:</span> [0-9]{13}'
    tmp_isbn = re.findall(pattern, res2.text, re.S)
    #print(tmp_isbn[0])
    if tmp_isbn:
        isbn = re.findall(r'[0-9]{13}', tmp_isbn[0])
        book["ISBN"] = isbn[0]
        print(book["ISBN"])
    else:
        book["ISBN"] = None
        print(book["ISBN"])
    return
