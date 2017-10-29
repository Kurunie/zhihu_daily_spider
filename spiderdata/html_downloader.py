# -*- coding: utf-8 -*-
from urllib import request, parse


class HtmlDownLoader:
    def download(self, url):
        req = request.Request(url)
        req.add_header('Host', 'daily.zhihu.com')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        resp = request.urlopen(req)
        if resp.getcode() != 200:
            return None
        return resp.read()