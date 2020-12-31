import matplotlib.pyplot as plt
import os
import numpy as np

plt.rcParams["font.family"] = 'Arial Unicode MS' #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置

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
    plt.bar(x, y1, width=width, label='本地运算', color='red')
    plt.bar(x + width, y2, width=width, label='远程运算', color='deepskyblue')
    # plt.bar(x + 2 * width, y3, width=width, label='useast4c', color='green')
    plt.xticks()
    plt.legend(loc="upper left")  # 防止label和图像重合显示不出来
    plt.ylabel('运算时长/ms')
    plt.xlabel('图片编号')
    # plt.rcParams['savefig.dpi'] = 300  # 图片像素
    # plt.rcParams['figure.dpi'] = 300  # 分辨率
    plt.rcParams['figure.figsize'] = (16.0, 9.0)  # 尺寸
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
    plt.bar(index, p1, width=width, label='传输时间', color='red')
    plt.bar(index, p2, width=width, bottom=p1, label='传输时间')
    plt.ylim(0, 100)
    plt.xticks(index)
    # plt.xticklabels([x for x in range(1, len(y2) + 1)])
    plt.legend(loc="upper left")  # 防止label和图像重合显示不出来
    plt.ylabel('百分比/%')
    plt.xlabel('图片编号')
    # plt.rcParams['savefig.dpi'] = 300  # 图片像素
    # plt.rcParams['figure.dpi'] = 300  # 分辨率
    plt.rcParams['figure.figsize'] = (16.0, 9.0)  # 尺寸
    # plt.title("measurement-latency")
    plt.savefig('../figures/f2.pdf')
    # plt.show()
    plt.close()
    # print(p)

if __name__ == "__main__":
    his_1()
    his_2()