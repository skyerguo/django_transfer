def calc_remote(image_path):
    import requests

    url = 'http://[2001:da8:270:2020:f816:3eff:fe7d:f719]:8000/imgProc/facialRecog/'

    files = {'img': open(image_path, 'rb')}
    res = requests.post(url, files=files)
    return res.text
    # print(res.text)
