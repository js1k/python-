from bs4 import BeautifulSoup

# 使用with语法可以open一个file, 最后不用close 会自动关闭
with open('test.html', 'r') as fin:
    html_doc = fin.read()

soup = BeautifulSoup(html_doc, 'html.parser')
#
# links = soup.find_all('a')
#
# for link in links:
#     print(link.name, link['href'], link.get_text())
#
# img = soup.find_all('img')
# print(img[0].attrs['src'])


# 先查找到目标块，然后再去查找目标元素
div_node = soup.find('div', id="content")

links = div_node.find_all('a')

for link in links:
    print(link.name, link['href'], link.get_text())

img = div_node.find('img')
print(img["src"])
