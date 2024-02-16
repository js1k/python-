import requests
from bs4 import BeautifulSoup
import pandas as pd

# 爬取豆瓣前250排行的数据， 共10个页面的HTML

# 构造分页数字列表
page_indexs = range(0, 250, 25)
list(page_indexs)
print(page_indexs)

def download_all_htmls():
    # 下载所有列表页面的HTML， 用于后续的分析
    htmls = []
    for idx in page_indexs:
        url = f"https://movie.douban.com/top250?start={idx}&filter="
        print("craw html:", url)
        r = requests.get(url)
        # if r.status_code != 200:
        #     raise Exception("error") 
        htmls.append(r.text)
        print(r.text)
    return htmls

htmls = download_all_htmls()
print(htmls[0])