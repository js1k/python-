"""
爬取图片， 并且下载图片
url: https://pic.netbian.com/4kmeinv/

爬取网页的requests
解析网页beautifulsoup

"""
# 解析图片的地址
from bs4 import BeautifulSoup
import os

# 获取网页源代码
# url = "https://pic.netbian.com/4kmeinv/"
url = "https://pic.netbian.com/4kfengjing/"
import requests

# 下载网页内容
def craw_html(url):
    resp = requests.get(url)
    resp.encoding = 'gbk'

    print(resp.status_code)

    html = resp.text
    return html
# print(html)

# 解析
def parse_and_download(html):
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.find_all('img')

    for img in imgs:
        src = img["src"]
        if "/uploads/" not in src:
            continue
        src = f"https://pic.netbian.com{src}"

        print(src)


        # 首先得到图片的本地文件地址
        # w 写入   wb写入二进制
        filename = os.path.basename(src)
        with open(f"美女图片/{filename}", "wb") as f:
            resp_img = requests.get(src)
            # resp.text是文本     resp.content是二进制流
            f.write(resp_img.content)

urls = ["https://pic.netbian.com/4kmeinv/"]+[
    f"https://pic.netbian.com/4kmeinv/index_{i}.html"
    for i in range(2, 11)
]

for url in urls:
    html = craw_html(url)
    parse_and_download(html)













