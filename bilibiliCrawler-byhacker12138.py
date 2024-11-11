import requests
import time
# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入json模块
import json
# TODO 记得更改你要的url和你自己的cookie


#urlinput = (input("请输入网址："))


cookie = "buvid3=86AB49DE-7F6E-0DE7-18AA-4F50638DAA9231847infoc; b_nut=1731207231; bsource=search_bing; _uuid=E919721C-310D1-61AD-ED5E-7105D344FDDD1032850infoc; buvid4=EDB3CED5-35B9-E4BC-366D-4036DADA38D632545-024111002-m4kjDELoiufSqb%2BsZ%2F20fQ%3D%3D; enable_web_push=DISABLE; buvid_fp=d1e13890a19ef5a48019142b235a7fd9; SESSDATA=0e2b0663%2C1746759248%2C75d58%2Ab1CjAo3jblSK69Qwhuz5BcfIHEjBDEoOZfEafNuwUkX0AsgOm3gSOEu3QqQeVjR1z7FZUSVlFYSXdxRU1UNzFIUlpMWV9ONmYtTlN3a1JCbE5BQ01qS1hKLUM4Z09pQS1VZzNhUVNENm1fNUZsOERoZmJrbm5pMDh6dnFTT0ZvZWpZRHFkdjVwdzhnIIEC; bili_jct=8341c5e4e69c1b1e655df3e14c770f79; DedeUserID=3546558857480758; DedeUserID__ckMd5=d52ec064589c37f3; CURRENT_FNVAL=4048; sid=7l2wjl00; rpdid=|(u)YlJ|lY~|0J'u~Juk|~J|Y; header_theme_version=CLOSE; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzE0ODU1MjIsImlhdCI6MTczMTIyNjI2MiwicGx0IjotMX0.h6ZPv7YK9kqMTbkAv-bABKJrvnRIZC7L3OeR99VN_A8; bili_ticket_expires=1731485462; bp_t_offset_3546558857480758=998098533565333504; b_lsid=BB110BADB_1931548F11E; home_feed_column=4; browser_resolution=1177-962"

#前置条件，包括待爬取网址url和head
url = "https://www.bilibili.com/"
head = {"User-Agent":"python-request/3.11.0"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
         # User-Agent 用户代理, 表示浏览器/设备基本身份信息
         "Referer": "https://www.bilibili.com/video/BV1454y187Er/",
         # Referer 防盗链 告诉服务器你请求链接是从哪里跳转过来的s
         "Cookie": cookie}





bv = "BV1Ccm1YdEKz"

url = url + f"/{bv}"




def main():
    # 发送请求
    response = requests.get(url=url, headers=headers)
    html = response.text
    print(html)
    # 解析数据: 提取视频标题
    title = re.findall('title="(.*?)"', html)[0]
    print(title)
    # 提取视频信息
    info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
    # info -> json字符串转成json字典
    json_data = json.loads(info)
    # 提取视频链接
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    print(video_url)
    # 提取音频链接
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    print(audio_url)
    video_content = requests.get(url=video_url, headers=headers).content
    # 获取音频内容
    audio_content = requests.get(url=audio_url, headers=headers).content
    # 保存数据
    with open('video\\' + title + '.mp4', mode='wb') as v:
        v.write(video_content)
    with open('video\\' + title + '.mp3', mode='wb') as a:
        a.write(audio_content)




main()
