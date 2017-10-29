# -*- coding: utf-8 -*-
from spiderdata import html_downloader, html_harser, url_manager
from spiderdata.models import Content
# 爬取知乎日报瞎扯内容


class Spider:
    def __init__(self):
        self.downloader = html_downloader.HtmlDownLoader()
        self.harser = html_harser.Harser()
        self.urls = url_manager.UrlManager()

    def craw(self, root_url):
        cont = self.downloader.download(root_url)
        urls = self.harser.index_harse(cont)
        self.urls.add_url(urls)
        list = []
        while self.urls.has_url():
            try:
                url = self.urls.get_url()
                if Content.objects.filter(urls=url).exists():
                    continue
                cont_2 = self.downloader.download(url)
                temp = self.harser.cont_harse(cont_2, url)
                list.append(temp)
            except Exception as e:
                print(Exception, ":", e)
                print('craw failed')
        return list

# r_url = 'https://daily.zhihu.com/'
# spider = Spider()
# print(spider.craw(r_url))


