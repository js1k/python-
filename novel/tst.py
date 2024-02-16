import requests
from bs4 import BeautifulSoup

# 获取所有章节链接
def get_novel_chapters():
    root_url = "https://www.biqudd.org/52_52155/"
    r = requests.get(root_url)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link:
            continue

        data.append(("https://www.biqudd.org/52_52155/"+link["href"], link.get_text()))
    return data

# 获取章节内容
def get_chapter_content(url):
    r = requests.get(url)
    r.encoding = 'gbk'
    soup = BeautifulSoup(r.text, "html.parser")
    content_div = soup.find('div', id="content")
    print(content_div)

    # 移除脚本或不需要的HTML元素
    [s.extract() for s in content_div(['script', 'style'])]

    # 将内容分割为行并保留换行
    lines = []
    for string in content_div.stripped_strings:
        # 处理特殊的HTML实体，如果有必要
        line = string.replace(u'\xa0', u' ')
        lines.append(line)

    # 将所有行合并成一个字符串，每行之间插入换行符
    text = '\n\n'.join(lines)
    return text


novel_chapters = get_novel_chapters()
total_cnt = len(novel_chapters)
idx = 0

for chapter in novel_chapters:
    idx += 1
    print(idx, total_cnt, chapter)
    # print(chapter)
    url, title = chapter
    with open("%s.txt"%title, "w") as file:
        file.write(get_chapter_content(url))
    # break