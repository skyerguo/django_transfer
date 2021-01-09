from multiprocessing import Pool, Process
import multiprocessing
import requests
import os

def single_request(ind, image_path):
    url = 'http://127.0.0.1:8000/imgProc/facialRecog/'
    files = {'img': open(image_path, 'rb')}
    res = requests.post(url, files=files)
    # return res.text, ind
    # print(res.text)
    return [ind, image_path, res.text]


def crowd_count_request(image_path):
    # url = 'http://10.177.53.226:8000/imgProc/crowdCnt/'
    url = 'http://127.0.0.1:8000/imgProc/crowdCnt/'
    files = {'img': open(image_path, 'rb')}
    res = requests.post(url, files=files)
    # return res.text, ind
    print(res.text)
    return [image_path, res.text]

def calc_remote_single(image_path):
    MAX_PROCESS = 1
    pool = Pool(processes=MAX_PROCESS)
    result = []
    for i in range(MAX_PROCESS):
        result.append(pool.apply_async(single_request, args=(i, image_path)))
    pool.close()
    pool.join()

    # for r in result:
    #     print(r.get())
    return result

def calc_remote_multi(image_source):
    MAX_PROCESS = 5
    pool = Pool(processes=MAX_PROCESS)
    result = []
    index = 0
    for image_name in os.listdir(image_source):
        image_path = os.path.join(image_source, image_name)
        result.append(pool.apply_async(single_request, args=(index, image_path)))
        index += 1
    pool.close()
    pool.join()
    
    # for r in result:
    #     print(r.get())
    return result

if __name__ == "__main__":
    print(crowd_count_request('./image/4.jpg'))