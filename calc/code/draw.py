import matplotlib.pyplot as plt
import os
import numpy as np
import json

plt.rcParams["font.family"] = 'Arial Unicode MS' #显示中文标签
plt.rcParams['axes.unicode_minus'] = False   #这两行需要手动设置

data_source = '../data/'
def his_1():
    data_path = os.path.join(data_source, 'single.txt')
    f = open(data_path, 'r')
    y1 = []
    y2 = []
    y3 = []
    for line in f:
        if 'cost_1' in line:
            y1.append(int(line.split(':')[1]))
        if 'cost_2' in line:
            y2.append(int(line.split(':')[1]))
        if 'transfer_time' in line:
            y3.append(int(line.split(':')[1]))
            # print('1111', line)
    f.close()

    size = len(y1)
    x = np.arange(size)
    total_width, n = 0.8, 2  # 有多少个类型，只需更改n即可
    width = total_width / n
    x = x - (total_width - width) / 2

    print(y1)
    print(y2)
    # print(y3)
    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.rcParams['figure.dpi'] = 300 #分辨率
    # plt.rcParams['figure.figsize'] = (16.0, 9.0)  # 尺寸

    plt.bar(x, y1, width=width, label='本地运算', color='red')
    plt.bar(x + width, y2, width=width, label='迁移运算', color='deepskyblue')
    # plt.bar(x + 2 * width, y3, width=width, label='useast4c', color='green')
    plt.xticks()
    plt.legend(loc="upper left")  # 防止label和图像重合显示不出来
    plt.ylabel('总时长/ms')
    plt.xlabel('图片编号')
    # plt.rcParams['savefig.dpi'] = 300  # 图片像素
    # plt.rcParams['figure.dpi'] = 300  # 分辨率

    # plt.title("measurement-latency")
    plt.savefig('../figures/f1.pdf')
    plt.close()
    # plt.show()

def his_2():
    data_path = os.path.join(data_source, 'single.txt')
    f = open(data_path, 'r')
    y1 = []
    y2 = []
    y3 = []
    for line in f:
        if 'cost_1' in line:
            y1.append(int(line.split(':')[1]))
        if 'cost_2' in line:
            y2.append(int(line.split(':')[1]))
        if 'transfer_time' in line:
            y3.append(int(line.split(':')[1]))
            # print('1111', line)
    f.close()
    p1 = []
    p2 = []
    for i in range(len(y2)):
        p1.append(y3[i]/(y2[i] + y3[i]) * 100)
        p2.append(y2[i]/(y2[i] + y3[i]) * 100)
    
    index = np.arange(len(y2))
    width = 0.4
    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.rcParams['figure.dpi'] = 300 #分辨率
    plt.bar(index, p1, width=width, label='传输时长占比', color='red')
    plt.bar(index, p2, width=width, bottom=p1, label='运算时长占比')
    plt.ylim(0, 100)
    plt.xticks()
    plt.legend(loc="upper left")  # 防止label和图像重合显示不出来
    plt.ylabel('百分比/%')
    plt.xlabel('图片编号')
    # plt.rcParams['figure.figsize'] = (16.0, 9.0)  # 尺寸
    # plt.title("measurement-latency")
    plt.savefig('../figures/f2.pdf')
    # plt.show()
    plt.close()
    # print(p)


def his_3():
    def add_text(x, y, data, fontsize=10):
        for y0, data0 in zip(y, data):
            plt.text(x, y0, round(data0, 1), fontsize=fontsize)

    data_path = os.path.join(data_source, 'multi.txt')
    f = open(data_path, 'r')
    y1 = []
    y2 = []
    y3 = []
    for line in f:
        if 'result_local' in line:
            y1.append(int(line.split(':')[1].split(' ')[-1]))
        if '[' in line:
            tmp = line.split('{')[1].split('}')[0]
            # print(tmp)
            tmp = json.loads('{' + tmp + '}')
            y2.append(int(tmp["result"][1]))
        if 'total_time_2' in line:
            y3.append(int(line.split(':')[1]))
            # print('1111', line)
    f.close()   

    index = np.arange(3)
    width = 0.6
    # print(y1)
    # tmp_data = np.array(y1)
    category_names = ["图片" + str(x) for x in range(1, 6)]
    category_colors = plt.get_cmap('RdYlGn')(np.linspace(0.15, 0.85, 5))
    # print(category_colors)

    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.rcParams['figure.dpi'] = 300 #分辨率
    # print(index)
    sum = 0
    accumulate = []
    for i in range(5):
        # print(category_colors[i])
        plt.bar(index[0], y1[i], width=width, label=category_names[i], bottom=sum, color=category_colors[i])
        sum += y1[i]
        accumulate.append(sum - y1[i] / 2 - 3000)
    add_text(index[0], accumulate, np.arange(1, 6))
    
    sum = 0
    accumulate = []
    for i in range(5):
        plt.bar(index[1], y2[i], width=width, bottom=sum, color=category_colors[i])
        sum += y2[i]
        accumulate.append(sum - y2[i] / 2 - 3000)
    add_text(index[1], accumulate, np.arange(1, 6))

    plt.bar(index[2], y3, width=width, label='迁移并行运算')
    
    x_item = ['本地单次运算', '迁移单次运算', '迁移并行运算']
    plt.xticks(index, x_item)
    
    plt.ylabel('运算时长/ms')
    plt.legend()
    # plt.xlabel('图片编号')
    plt.savefig('../figures/f3.pdf')
    # plt.show()
    plt.close()


if __name__ == "__main__":
    # his_1()
    # his_2()
    his_3()
    # 编号、大小、人数、运行时间