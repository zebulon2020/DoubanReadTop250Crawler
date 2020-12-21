import pandas

def save_to_csv(books):
    '''
    将全部书籍的信息保存到csv文件中
    '''
    df = pandas.DataFrame(books)
    df.to_csv("BookDouban250.csv",header=['排名','书名','作者','译者','出版社','出版日期','价格','豆瓣链接','评分','简介','图片链接','ISBN'],index=False)