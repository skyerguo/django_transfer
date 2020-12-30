from multiprocessing import Pool, Process
import multiprocessing
import requests
import os

MAX_PROCESS = 1

def single_request(ind, image_path):
    url = 'http://[2001:da8:270:2020:f816:3eff:fe7d:f719]:8000/imgProc/facialRecog/'
    # url = 'http://127.0.0.1:8000/imgProc/facialRecog/'
    files = {'img': open(image_path, 'rb')}
    res = requests.post(url, files=files)
    # return res.text, ind
    print(res.text)
    return ind



def calc_remote(image_path):
    pool = Pool(processes=MAX_PROCESS)
    result = []
    for i in range(MAX_PROCESS):
        result.append(pool.apply_async(single_request, args=(i, image_path)))
    pool.close()
    pool.join()

    # for r in result:
    #     print(r.get())
    return result


