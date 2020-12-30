import requests

url = 'http://[2001:da8:270:2020:f816:3eff:fe7d:f719]:8000/imgProc/facialRecog/'

files = {'img': open('./1.jpg', 'rb')}
res = requests.post(url, files=files)
print(res.text)
