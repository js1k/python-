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
        print(dd)
        link = dd.find("a")
        if not link:
            continue

        data.append(("https://www.biqudd.org/52_52155/"+link["href"], link.get_text()))
    return data
        # print(link)

# 获取章节内容
def get_chapter_content(url):
    r = requests.get(url)
    r.encoding = 'gbk'
    soup = BeautifulSoup(r.text, "html.parser")
    # return soup.find('div', id="content").get_text()

    content_div = soup.find('div', id="content")
    print('content_div', content_div)
    # return content_div.get_text()

    # 替换 <br> 标签为换行符
    for br in content_div.find_all("br"):
        br.replace_with("\n")

    # 获取处理后的文本内容
    text = content_div.get_text()
    # return text
    print(111, text)

    # 可选：替换连续的空白字符为一个空格
    # text = ' '.join(text.split())
    text = text.replace('笔趣阁顶点 www.biqudd.org，最快更新九龙归一诀 ！', "")

    start = text.find("“")  # 假设故事文本从第一个引号开始
    if start != -1:
        text = text[start:]

    print('text===', text)
    return text

novel_chapters = get_novel_chapters()
total_cnt = len(novel_chapters)
idx = 0

for chapter in novel_chapters:
    idx += 1
    print(idx, total_cnt, chapter)
    # print(chapter)
    url, title = chapter
    with open("%s.txt"%title, "w", encoding="utf-8") as file:
        file.write(get_chapter_content(url))
    break