import re

import requests
from utils import url_manager
from bs4 import BeautifulSoup

root_url = 'http://www.crazyant.net'
urls = url_manager.UrlManager()
urls.add_new_url(root_url)

fout = open('craw_all_pages.txt', 'w')
while urls.has_new_url():
    # 取出url
    curr_url = urls.get_url()

    # 爬取页面内容
    r = requests.get(curr_url, timeout = 3)
    if r.status_code != 200:
        print('error, return status_code is not 200', curr_url)
        continue

    # 进行解析
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title.string

    # soup.title 会得到title这个节点    string会得到里面的文字
    fout.write("%s\t%s\n" % (curr_url, title))
    fout.flush()
    print("success: %s, %s, %d" % (curr_url, title, len(urls.new_urls)))

    # 爬取到所有新的url，添加到url管理器中
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if(href is None):
            continue
        # 判断爬取到的Url是否符合我们的条件时， 用政策表达式
        pattern = r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern, href):
            urls.add_new_url(href)

fout.close()