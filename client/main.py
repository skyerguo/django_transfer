from facialRecog import calc_local
from remoteCalc import calc_remote_single, calc_remote_multi
import time 
import resource
import json
import os

def compare_single_picture(image_path):
    res, cost_1 = calc_local(image_path)
    print("单次本地计算时间: ", cost_1, "ms")
    print("单次本地人脸计数结果: ", res)
    start_time = int(round(time.time() * 1000))
    res = calc_remote_single(image_path)
    # print(res)
    for r in res:
        # print(r.get())
        tmp = json.loads(r.get()[-1])
        # print(tmp["result"])
        print("单次远程人脸计数结果: ", tmp["result"][0])
        cost_2 = tmp["result"][1]
    end_time = int(round(time.time() * 1000))

    total_time_2 = end_time - start_time
    transfer_time_2 = total_time_2 - cost_2
    print("单次远程计算时间: ", cost_2, "ms")
    print("单次远程传输时间: ", transfer_time_2, "ms")


def compare_multi_picture(image_source): 
    start_time = int(round(time.time() * 1000))
    for image_name in os.listdir(image_source):
        image_path = os.path.join(image_source, image_name)
        res1, cost_1 = calc_local(image_path)
        print("并行本地计算时间: ", cost_1, "ms")
        print("并行本地人脸计数结果: ", res1)
        # print("result_local: ", res1, cost_1)
    end_time = int(round(time.time() * 1000))
    total_time_1 = end_time - start_time
    print("并行本地计算总时间: ", total_time_1, "ms")
    
    start_time = int(round(time.time() * 1000))
    res = calc_remote_multi(image_source)
    cost_2 = 0
    for r in res:
        print(r.get())
        tmp = json.loads(r.get()[-1])
        # print(tmp)
        cost_2 += int(tmp["result"][1])
    end_time = int(round(time.time() * 1000))
    total_time_2 = end_time - start_time
    print("并行远程计算总时间: ", total_time_2,  "ms")
    transfer_time_2 = total_time_2 - cost_2
    print("并行远程传输总时间: ", transfer_time_2,  "ms")


if __name__ == '__main__':
    image_source = "./image"
    for image_name in os.listdir(image_source):
        image_path = os.path.join(image_source, image_name)
        compare_single_picture(image_path)
    print('---单次测量结束，即将进行并行测量---')
    time.sleep(5)
    compare_multi_picture(image_source)
    print('---并行测量结束---')