from facialRecog import calc_local
from remoteCalc import calc_remote
import time 
import resource
import os

def compare_single_picture(image_path):
    res, cost_1 = calc_local(image_path)
    print(cost_1)
    start_time = int(round(time.time() * 1000))
    res = calc_remote(image_path)
    print(res)
    end_time = int(round(time.time() * 1000))

    total_time_2 = end_time - start_time
    transfer_time_2 = total_time_2 - cost_2
    print(transfer_time_2)


if __name__ == '__main__':
    image_source = "./image"
    for image_name in os.listdir(image_source):
        image_path = os.path.join(image_source, image_name)
        compare_single_picture(image_path)
        break
        # print(image_path)