# -*- coding: utf-8 -*-
class UrlManager:
    def __init__(self):
        self.urls = set()

    def add_url(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.urls.add(url)

    def has_url(self):
        return len(self.urls) != 0

    def get_url(self):
        url = self.urls.pop()
        return url
