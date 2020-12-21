import matplotlib.pyplot as plt
import numpy as np
import json
import matplotlib.font_manager as font_manager


def count_publisher():
    with open('book_detail.json', 'r', encoding='UTF-8') as f:
        json_array = json.loads(f.read())

    # 绘制出版社分布直方图，x轴为出版社，y轴为top250书籍所属的出版社数量
    pubs = []
    for book in json_array:
        pub = book["book_publisher"]
        pubs.append(pub)
    print(len(pubs))
    print(pubs)

    pub_list = []
    count_list = []

    for pub in pubs:
        if pub not in pub_list:
            count = pubs.count(pub)
            pub_list.append(pub)
            count_list.append(count)

    # 设置显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

    # 降序排列,如果从小到大排序，argsort参数是直接factorData，如果从大到小排序，使用-factorData
    factorData = np.array(count_list)
    xaxislabel = np.array(pub_list)
    x = xaxislabel[np.argsort(-factorData)]
    y = factorData[np.argsort(-factorData)]

    plt.figure(figsize=(20, 15))

    plt.xticks(np.arange(len(xaxislabel)), x, rotation=-90, fontsize=8)
    rects = plt.bar(np.arange(len(xaxislabel)), y)

    # rects = plt.bar(range(len(count_list)), count_list, color='r',
    #         tick_label=pub_list, facecolor='#9999ff', edgecolor='white')

    # 在柱状上方显示数字
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height,
                 str(height), size=15, ha='center', va='bottom')

    # 调节横坐标的倾斜度，rotation是度数，以及设置刻度字体大小
    #plt.xticks(rotation=-90, fontsize=8)
    plt.yticks(fontsize=20)
    plt.legend()
    plt.title('top250出版社统计', fontsize=20)
    plt.savefig('./bar_publisher.jpg')
    #plt.show()
    print("出版社分布统计的直方图保存在工程目录下的bar_publisher.jpg")
