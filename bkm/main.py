from bs4 import BeautifulSoup
import requests
import html

url = "https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89"

r = requests.get(url)
if r.status_code != 200:
    raise Exception()
# r.encoding = "utf-8"

html_doc = r.text
soup = BeautifulSoup(html_doc, "html.parser")

html_shidai = soup.find_all('table', class_='rdexn')

ar = []
# len(html_shidai) 可取其长度
# print(len(html_shidai))
for index, shidai_node in enumerate(html_shidai):
    tr_list = shidai_node.select('tbody tr')
    # print(len(tr_list))
    tmp = {
        # "order": tr_list[0].attrs.get('data-type'),
        "img": "",
        "cn_name": "",
        "en_name": "",
        "jap_name": "",
        "shuxing": []
    }
    for idx, row in enumerate(tr_list):
        td = row.select("td")
        # print(row)
        if len(td) >3 and td[3]:
            # html.unescape() 可以处理转义
            tmp["cn_name"] = td[3].get_text().strip()
            tmp["en_name"] = td[5].get_text().strip()
            tmp["jap_name"] = td[4].get_text().strip()
        # print(idx, td)
        # print(idx, tr[idx])
        # tmp["img"] = ''
        # tmp["cn_name"] = td[idx].get_txt()
        # tmp["cn_name"] = td[3].get_txt()
        # for ix, ix_row in enumerate(td):
        #     # print(ix)
        #     tmp["cn_name"] = td[ix].get_txt()
    # ar[index]["order"] = tr[0].attrs.get('data-type')
        
    ar.append([tmp])
    print(ar)
    print('\n')