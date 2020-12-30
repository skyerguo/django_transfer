from facialRecog import calc_local
from remoteCalc import calc_remote
import time 
import resource
import os

if __name__ == '__main__':
    image_path = "./1.jpg"
    res, cost_1 = calc_local(image_path)
    print(cost_1)
    start_time = int(round(time.time() * 1000))
    res, cost_2 = calc_remote(image_path)
    end_time = int(round(time.time() * 1000))

    total_time_2 = end_time - start_time
    transfer_time_2 = total_time_2 - cost_2
