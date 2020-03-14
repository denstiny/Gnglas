import re 
import requests
import os
url = 'https://www.hippopx.com/zh'
img_url = '" src="(https://.*?\.jpg)"'
def new1():
    reques = requests.get(url)
    reques = reques.content.decode("utf-8")
    res = re.findall(img_url,reques,re.S)
    return res 
def tow():
    name = 0
    jpg_url = new1()
    for jpf in jpg_url:
        print("正在下载图片.....    ")
        a=requests.get(jpf)
        name += 1
        names=str(name) + '.jpg'
        #print(a.content)
        with open(names, 'wb') as f:
            f.write(a.content)
tow()
