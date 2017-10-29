# -*- coding: utf-8 -*-
from spiderdata import html_downloader, html_harser, url_manager, html_output
# 爬取知乎日报瞎扯内容


class Spider:
    def __init__(self):
        self.downloader = html_downloader.HtmlDownLoader()
        self.harser = html_harser.Harser()
        self.urls = url_manager.UrlManager()
        self.output = html_output.HtmlOutpuer()

    def craw(self, root_url):
        cont = self.downloader.download(root_url)
        urls = self.harser.index_harse(cont)
        self.urls.add_url(urls)
        while self.urls.has_url():
            try:
                url = self.urls.get_url()
                cont_2 = self.downloader.download(url)
                self.harser.cont_harse(cont_2, url)
            except Exception as e:
                print(Exception, ":", e)
                print('craw failed')

