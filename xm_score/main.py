from urllib.parse import urlencode
from bs4 import BeautifulSoup

import requests
url = "https://life.httpcn.com/xingming.asp"

def get_score(xing, ming):
    data = {
        "isbz": "0",
        "sex": "1",
        "data_type": "0",
        "year": "1980",
        "month": "2",
        "day": "12",
        "hour": "23",
        "minute": "10",
        "wxxy": "0",
        "pid": "",
        "cid": "",
        "xishen": "金".encode("gb2312"),
        "yongshen": "金".encode("gb2312"),
        "xing": xing.encode("gb2312"),
        "ming": ming.encode("gb2312"),
        "check_agree": "agree",
        "act": "submit"
    }

    headers = {
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://life.httpcn.com/xingming.asp",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": "Hm_lvt_668a2b1ccec82d575177212da2570e5d=1707750220; ASPSESSIONIDQEASARDR=CFBFLMIAOOPMIPEOLMGCIENB; ASPSESSIONIDSEDTASCQ=IEIBHFDBHKDFPEFHNBGNDKAC; Hm_lpvt_668a2b1ccec82d575177212da2570e5d=1707827121"
    }

    r = requests.get(url, data = urlencode(data), headers=headers)

    r.encoding = "gb2312"
    # print(r.status_code)
    # print(r.text)

    soup = BeautifulSoup(r.text, "html.parser")

    divs = soup.find_all("div", class_="chaxun_b")

    bazi, wuge = 0, 0
    for div in divs:
        # print('divs\n\n', div)
        if "姓名五格评分" not in div.get_text():
            continue
        # print(div)

        fonts = div.find_all("font")
        print(fonts)
        bazi = fonts[0].get_text().replace('分', "").strip()

    return "%s%s"%(xing, ming),bazi

# print(get_score("鲍", "斌"))

with open("input.txt") as fin, open("out.txt", "w") as fout:
    for line in fin:
        line = line.strip()
        xingming, bazi = get_score("鲍", line)
        fout.write("%s\t%s\t\n"%(xingming, bazi))
