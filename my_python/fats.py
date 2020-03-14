import re 
import requests
from bs4 import BeautifulSoup
import time
print("天使议会，自动发帖小程序 \n\t\t\t---作者：Gnglas")
#爬取帖子 
A = 0
a = 0
print("")
_key = input("请输入key（key是存储葫芦侠的帐号，需要进行抓包获取）:")

while(A <= 19):
    A += 1
    
    head_url = "https://wangejiba.com/page/"+str(A) #首页地址    
    head = {

        'Cookie':'__gads=ID=4a32d87d7c539748:T=1582730628:S=ALNI_MbbMjCJJEPSbMFjM-0w_HwRhSDwAA; hyphp_lang=zh-CN; Hm_lvt_a5f7985370bad89db443f1146005a35b=1582730629,1582740408; PHPSESSID=71v58e6q1b3eusdtmen3lsr0k6; HYBBS_HEX=k9YQIqhn%25252FF3WOaBqKi6llzgXXy5YZ6REKLdJq2YJzxx%25252FJEkYSkh4gQPuzh%252B7sc7VmWcqncpPbdDl5thxQvIuL5Xjj98BgkcXVYoQo02OxQlOJXf2x8WYhHvCF47xezbRefKjXI4e7%25252Flkyi%25252FXIZkZk%25252FkfUZw%253D; Hm_lpvt_a5f7985370bad89db443f1146005a35b=1582741168',
        'Host':'bbs.liuxingw.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
        }


    html = requests.get(head_url,headers = head) # 爬取首页html源代码
    rez = '<h2 class="entry-title"><a href="(.*?)" '
    list_url = re.findall(rez,html.text,re.S)  #爬取帖子列表
    print(list_url)
    for html_urls in list_url:
        a += 1
        html = str(html_urls) 
        html = requests.get(url = html_urls,headers = head)
        print(html)
        bs = BeautifulSoup(html.content,'html.parser') # bs存储html源代码
        tet = bs.select("#body > div.site > div.site-content.container > div > div.col-lg-9 > div > main > article > div.entry-wrapper > div.entry-content.u-clearfix")
        txt_name = str(a)+'.txt'
        for tet in tet: 
            tet = tet.text
            tet = str(tet)
            with open(txt_name,'w') as f:
                f.write(tet)
        print('第%d篇帖子写入成功'%(a))
        time.sleep(3) 

#发帖函数
b = 0
while(b < 999):
    url = "http://floor.huluxia.com:80/post/create/ANDROID/2.0?"
    b += 1
    ms =[] 
    with open(str(b)+'.txt') as f:
        for line in f.readlines():
            ms = str(ms) + str(line) 


#定义请求头
    head = {

        'platform':'2',		
        'gkey':'000000',		
        'app_version':'4.0.1.5.4',		
        'versioncode':'289',		
        'market_id':'tool_web',		
        '_key':_key,		
        'device_code':'%5Bw%5D02%3A00%3A00%3A00%3A00%3A00%5Bd%5D1dac64cb-9509-48ee-8ed5-cf8ca40eaf5f HTTP/1.1',
        'Connection':'close',
        'Content-Type':'application/x-www-form-urlencoded',
        'Content-Length':'2600',
        'Host':'floor.huluxia.com',
        'Accept-Encoding':'gzip',
        'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G9500 Build/R16NW'
    }
#定义发送的数据
    dat = {
        
        '_key':_key,
        'cat_id':'44',
        'tag_id':'4403',
        'type':'0',
        'title':'【W.J.X】'+str(b)+'软件教程',
        'detail':ms,
        'patcha':'',
        'voice':'',
        'lng':'116.395097',
        'lat':'29.529995',
        'images':'images=g3/M01/6D/F2/wKgBOV5XZDKAHNnGAAJt5ZbNy3Q158.jpg,g3/M01/6D/F2/wKgBOV5XZDOAYOepAALExscJw-s528.jpg,g3/M01/6D/F2/wKgBOV5XZDOAbAOsAACCtnhFQ2w492.jpg,g3/M01/6D/F2/wKgBOV5XZDOAY1RZAABnXaKa7mg240.jpg',
    
        'user_ids':'',
        'recommendTopics':'',

        }
    
    res = requests.post(url,data = dat,headers = head)
    print(res.status_code)
    rez = '"msg":"(.*?)"'
    hu = res.content.decode("utf-8")
    #print(hu)
    hus = re.findall(rez,hu,re.S)
    print(hus)
    print("发送完毕，休息一会")
    print("休息完毕，继续开始")
