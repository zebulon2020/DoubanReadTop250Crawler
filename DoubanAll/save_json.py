import json

def save_to_json(books):
    '''
    将全部书籍的信息保存到json文件中
    '''
    #json_data = json.loads(str(books).replace("'", "\""))
    with open('book_detail.json', 'w', encoding='UTF-8') as f:
        json.dump(books, f, ensure_ascii=False)