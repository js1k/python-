from pip._internal.utils import urls


class UrlManager(object):
     # url管理器

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        # None 不存在   len长度为零
        if url is None or len(url) == 0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    # 批量添加url， 则调用单个添加方法
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_url(self):
        if self.has_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        return len(self.new_urls) > 0

if __name__ == '__main__':
    # 别的模块引用这个模块，就不会引入以及执行下面的代码  此判断的作用
    url_manager = UrlManager()

    url_manager.add_new_url('url1')
    url_manager.add_new_urls(['url1', 'url2'])
    print(url_manager.new_urls, url_manager.old_urls)

    print('#'*30)
    new_url = url_manager.get_url()
    print(url_manager.new_urls, url_manager.old_urls )

    print('#'*30)
    new_url = url_manager.get_url()
    print(url_manager.new_urls, url_manager.old_urls)

    print('#'*30)
    print(url_manager.has_new_url() )



