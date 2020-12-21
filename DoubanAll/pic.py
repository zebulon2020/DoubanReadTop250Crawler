import json
import os
import requests


def crawl_image():
    '''
    爬取书籍的图片的url，调用down_pic函数下载图片
    '''
    with open('book_detail.json', 'r', encoding='UTF-8') as file:
        json_array = json.loads(file.read())

    for book in json_array:
        name = book['book_name']
        pic_link = book['pic_url']
        number = book['num']
        down_pic(name, pic_link, number)


def down_pic(name, pic_url, number):
    '''
    根据图片url下载书籍图片，保存在以name命名的文件夹
    '''
    print(pic_url)
    path = 'data/' + 'pics/' + str(number) + '.' + name + '/'
    if not os.path.exists(path):
        os.makedirs(path)

    try:
        pic = requests.get(pic_url, timeout=15)
        string = name + '.jpg'
        with open(path+string, 'wb') as f:
            f.write(pic.content)
            print('成功下载' + name + '图片')
    except Exception as e:
        print('下载' + name + '图片失败')
        print(e)
