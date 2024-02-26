from bs4 import BeautifulSoup
import requests
import html
import re
from selenium import webdriver

url = "https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89"

r = requests.get(url)
if r.status_code != 200:
    raise Exception()
# r.encoding = "utf-8"

html_doc = r.text
soup = BeautifulSoup(html_doc, "html.parser")

html_shidai = soup.find_all('table', class_='rdexn')

# 设置总空数组
ar = []
# len(html_shidai) 可取其长度

# 循环总的table 找到每个table下的tr 
# 再循环tr
driver = webdriver.Chrome()
driver.get(url)
for index, shidai_node in enumerate(html_shidai):
    tr_list = shidai_node.select('tbody tr:not(thead tr)')
    for idx, row in enumerate(tr_list):
        tmp = {
            "order": "",
            "img": "",
            "cn_name": "",
            "en_name": "",
            "jap_name": "",
            "shuxing": []
        }
        
        # if row:
        td = row.select("td")

        if td:
        # html.unescape() 可以处理转义
            tmp["cn_name"] = td[3].get_text().strip().replace("#", "")
            tmp["en_name"] = td[5].get_text().strip().replace("#", "")
            tmp["jap_name"] = td[4].get_text().strip().replace("#", "")
            tmp["order"] = td[0].get_text().strip().replace("#", "")
            if td[6].find('a'):
                st = td[6].attrs
                ca = '.' + st["class"][0] + '.' +  st["class"][1] + '.' +  st["class"][2]
                # s,*rest = st["class"]
                el = driver.find_element("css selector" ,ca)
                tmp["shuxing"].append({"name": td[6].get_text().strip(), "bg": el.value_of_css_property("background-color")})
            if td[7].find('a'):
                st = td[7].attrs
                ca = '.' + st["class"][0] + '.' +  st["class"][1] + '.' +  st["class"][2]
                el = driver.find_element("css selector" ,ca)
                tmp["shuxing"].append({"name": td[7].get_text().strip(), "bg": el.value_of_css_property("background-color")})
        ar.append(tmp)    
    print(ar)
    print('\n')