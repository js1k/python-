
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.cnblogs.com/"


def craw_page(page_index):
    data = {
        "CategoryId": 808,
        "CategoryType": "SiteHome",
        "ItemListActionName": "AggSitePostList",
        "PageIndex": 3,
        "ParentCategoryId": 0,
        "TotalPostCount": 2000
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": "_cc_id=452dffe45355d4c9b3fe104122fedcfd; cto_bundle=74LWcl92RWs4NTZBcGlaYlREdmZCZlZ6WmlzTzZzNzd0bkVQJTJCb2NZZHNxa1BQNTZsOXpxalo1QzZIY0JQNXp6czg4bXJDa0N2UiUyQmkwRjBkZ0VhVURhc1VYWlNHZTNwZzRiTTNKSyUyQllPOFJNNnFDZHFGZGJDYkcwUiUyQkNCWjlxU2gzbGpjNGdrZHRGNk90cm9EbVFTZlZMSTFJdyUzRCUzRA; .AspNetCore.Antiforgery.b8-pDmTq1XM=CfDJ8DZoAyJmInJHoSwqM1IbzdR3fed22N6YY7K2jqVINCMaaYw0EJGprirG4NsthXA8FfV39IGMoeZaMxfKjBeFAl7_I2xKG4vj0YE2glGi5k7Bu5Hwua4VzixeRTNJZ7iQC3pctOsnJMevXVbrPBAB_Nc; _ga=GA1.1.178159858.1687706791; _pk_id.1.1edd=8174bdd4eaaafd0f.1704381454.; __gads=ID=90abf6ed117f32b8:T=1687706791:RT=1706108761:S=ALNI_MaMeKg92xAz_xLsAmsBtaf2olADRg; __gpi=UID=00000c182848794a:T=1687706791:RT=1706108761:S=ALNI_MYAptEYMz2Ck6BwP0fJhegB70Mkgw; Hm_lvt_866c9be12d4a814454792b1fd0fed295=1707912261; Hm_lpvt_866c9be12d4a814454792b1fd0fed295=1707912261; _ga_M95P3TTWJZ=GS1.1.1707912261.7.0.1707912266.0.0.0"
    }
    resp = requests.post(url, data = json.dumps(data), headers = headers)
    return resp.text


def parse_data(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("article", class_="post-item")

    datas = []
    json_data = []
    for article in articles:
        # print(article)
        json_obj = {}
        link = article.find("a", class_="post-item-title")
        title = link.get_text()
        href = link["href"]

        author = article.find('a', class_="post-item-author").get_text()

        # print(title, href)
        print('author', author)

        icon_digg = 0
        icon_comment = 0
        icon_views = 0

        for a in article.find_all('a'):
            if "icon_digg" in str(a):
                icon_digg = a.find("span").get_text()
            if "icon_comment" in str(a):
                icon_comment = a.find("span").get_text()
            if "icon_views" in str(a):
                icon_views = a.find("span").get_text()
        datas.append([title, href, author, icon_digg, icon_comment, icon_views])
        json_obj = {
            "title": title,
            "href": href,
            "icon_digg": icon_digg,
            "icon_comment": icon_comment,
            "icon_views": icon_views
        }
        json_data.append(json_obj)

        return [datas, json_data]

all_datas = []
all_json_data = []

for page in range(50):
    print('正在爬取', page)
    html = craw_page(page)
    datas = parse_data(html)
    all_datas.extend(datas[0])
    all_json_data.extend(datas[1])

import pandas as pd

df = pd.DataFrame(all_datas, columns = ["title", "href", "author", "icon_digg", "icon_comment", "icon_views"])
df.to_excel('博客园200页文章信息.xlsx', index=False)
df1 = pd.DataFrame(all_json_data)

with open("data.json", "w") as json_file:
    json.dump(all_json_data, json_file, indent=2)