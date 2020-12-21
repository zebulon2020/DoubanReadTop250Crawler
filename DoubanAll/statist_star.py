import matplotlib.pyplot as plt
import numpy as np
import json
import matplotlib.font_manager as font_manager


def statist():
    with open('book_detail.json', 'r', encoding='UTF-8') as file:
        json_array = json.loads(file.read())
    scores = []

    for book in json_array:
        score = float(book['book_star'])
        scores.append(score)
    print(scores)

    size1 = 0  # 大于等于9.5分的书籍的数目
    size2 = 0  # 大于等于9.0小于9.5分的书籍的数目
    size3 = 0  # 大于等于8.5分小于9.0分的书籍的数目
    size4 = 0  # 大于等于8.0分小于8.5分的书籍的数目

    for score in scores:
        if score >= 9.5:
            size1 += 1
        elif score >= 9.0:
            size2 += 1
        elif score >= 8.5:
            size3 += 1
        else:
            size4 += 1

    labels = '>=9.5', '[9.0, 9.5)', '[8.5,9.0)', '[8.0,8.5)'
    sizes = [size1, size2, size3, size4]

    explode = (0, 0, 0, 0.1)
    plt.figure(figsize=(10, 10))
    _, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig('./pie_result.jpg')
    #plt.show()
    print("top250书籍评分的饼状图保存在工程目录下的pie_result.jpg")
