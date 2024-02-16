import requests
from bs4 import BeautifulSoup
import json

url = "https://maimai.cn/sdk/web/content/get_list"

# ctrl alt l

def get_data(page):
    params = {
        "api": "contact/feed/v5/d1feed",
        "u": "157448227",
        "page": page,
        "appid": 1,
        "before_id": "1820996255"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://maimai.cn/feed_list",
        "X-Csrf-Token": "uRbmRB3J-YZ6nth6DWtJSnvABv1CGIvhnqJs",
        "Cookie": "seid=s1707745340507; guid=GBgYBBwfBBscHgQeHFYHGBseGxgaHBsdG1YcGQQdGR8FQ1hLTEt5ChoEGgQaBBoYGwVPR0VYQmkKA0VBSU9tCk9BQ0YKBmZnfmJhAgocGQQdGR8FXkNhSE99T0ZaWmsKAx11Hxt1GhsKcgp5ZQpJS2cKRk9eRGMKEUJZRV5EQ0lLZwIKGgQfBUtGRkNQRWc=; csrftoken=uRbmRB3J-YZ6nth6DWtJSnvABv1CGIvhnqJs; AGL_USER_ID=b81883e7-6d07-4efe-b575-9a23c5885529; _buuid=00e7459e-937e-4162-a1d1-dc6e01c13900; browser_fingerprint=1D8BA63D; gdxidpyhxdE=iv%2FG1XqBVP3BhB25%2BjAycrfd8La1jvD0IIQr4nIANGWxlJqbXDi7McbEgxrtwwpotkGq2nZdu%5CMI5ekW4Y6NMv73p6ZLZ4MJC69iSNm3oYm%2Burz1wM%2FprffuL2Y%2FjzdvXPRTP4WgqKLW0SmY7%2FcjoYmt%5CAeHCSV8dKohEGYgN9V5OCHE%3A1707746251387; u=157448227; u.sig=xXPzGotMcJEGYt-1_0mKf0Cvob0; access_token=1.627f005b29d8fa276ab4cde835ffe0a0; access_token.sig=7q16qaTCfCMINqg-0ojGo0quF9I; u=157448227; u.sig=xXPzGotMcJEGYt-1_0mKf0Cvob0; access_token=1.627f005b29d8fa276ab4cde835ffe0a0; access_token.sig=7q16qaTCfCMINqg-0ojGo0quF9I; channel=www; channel.sig=tNJvAmArXf-qy3NgrB7afdGlanM; maimai_version=4.0.0; maimai_version.sig=kbniK4IntVXmJq6Vmvk3iHsSv-Y; session=eyJzZWNyZXQiOiI4VE9OOXhxMDlRbmVoTElNQzRqeklfbS0iLCJ1IjoiMTU3NDQ4MjI3IiwiX2V4cGlyZSI6MTcwNzgzMTc2Nzk4OCwiX21heEFnZSI6ODY0MDAwMDB9; session.sig=9ffuFBWnNCnB3hjW3r7gd7EKxwk"
    }
    print('headers-------', params["page"])
    resp = requests.get(url, params=params, headers=headers)
    # print(resp.status_code)
    # print(resp.text)

    # soup = BeautifulSoup(resp.text, "html.parser")
    # print(soup.get_text())
    data = json.loads(resp.text)

    datas = []
    idx = 0
    for txt in data["list"]:
        idx = idx + 1
        datas.append(txt["style1"]["text"])
        params["page"] = params["page"] + 1
    return datas

        # get_data(url)


with open('脉脉结果.txt', 'w', encoding="utf8") as f:
    for page in range(1, 10+1):
        print("craw page", page)
        datas = get_data(page)
        f.write("\n".join(datas) + "\n\n\n")





