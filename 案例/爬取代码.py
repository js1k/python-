url = "http://tianqi.2345.com/Pc/GetHistory"



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
}

import requests
import pandas as pd

def craw_table(year, month):
    # 提供年份和月份
    params = {
        "areaInfo[areaId]": 54511,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month
    }

    resp = requests.get(url, params=params, headers=headers)
    print(resp.status_code)
    # print(resp.text)

    data = resp.json()["data"]
    # print(data)

    # data frame
    df = pd.read_html(data)[0]
    print(df.head())
    return df

df = craw_table(2015, 10)
print(df.head() )