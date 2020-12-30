# def calc_remote(image_path):
#     import requests

#     url = 'http://[2001:da8:270:2020:f816:3eff:fe7d:f719]:8000/imgProc/facialRecog/'

#     files = {'img': open(image_path, 'rb')}
#     res = requests.post(url, files=files)
#     return res.text
#     # print(res.text)

from multiprocessing import Process
import requests
import os

MAX_PROCESS = 1

def single_request(ind, image_path):
    url = 'http://[2001:da8:270:2020:f816:3eff:fe7d:f719]:8000/imgProc/facialRecog/'
    # url = 'http://127.0.0.1:8000/imgProc/facialRecog/'
    files = {'img': open(image_path, 'rb')}
    res = requests.post(url, files=files)
    return res.text, ind
    print(res.text)
    print(ind)

def calc_remote(image_path):
    pools = []
    for i in range(MAX_PROCESS):
        p = Process(target=single_request, args=(i,))
        p.start()

    for process in pools:
        process.join()

