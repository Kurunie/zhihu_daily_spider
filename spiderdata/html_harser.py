# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from spiderdata.models import Content

class Harser:

    def _get_urls(self, soup):
        urls = set()
        links = soup.find_all('a', href=re.compile(r"/story/\d+"))
        for link in links:
            title = link.find('span', class_="title")
            if title.get_text() == u"瞎扯 · 如何正确地吐槽":
                urls.add("https://daily.zhihu.com" + link['href'])
        return urls

    # def link_mysql(self):
    #     connection = pymysql.connect(host='localhost', user='kurunie', password='snowewhite132', db='zhihu_daily', charset='utf8mb4')
    #     try:
    #         with connection.cursor() as cursor:
    #             sql = "insert ignore into `content` (`urls`,`urlques`,`author`,`urlans`) value(%s, %s, %s, %s)"
    #             cursor.execute('select * from content')
    #             rows = cursor.fetchall()
    #             for row in rows:
    #                 if row[1] == self.urls:
    #                     break
    #             else:
    #                 cursor.execute(sql, (self.urls, self.urlques, self.author, self.ans))
    #                 connection.commit()
    #     finally:
    #         connection.close()

    def cont_harse(self, cont, url):
        soup = BeautifulSoup(cont, 'html.parser')
        question = soup.find('div', class_="question")
        data = Content()
        data.urls = url
        data.urlques = question.h2.string
        anss = soup.find_all('div', class_="answer")
        temp1 = ""
        temp2 = ""
        for ans in anss:
            author = ans.find('span', class_="author").get_text().rstrip('，')
            cont = ans.find('div', class_="content").get_text()
            # print(cont)
            temp1 = (temp1 + '@@' + author) if len(temp1) != 0 else author
            temp2 = (temp2 + '@@' + cont) if len(temp2) != 0 else cont
        data.author = temp1
        data.urlans = temp2
        data.save()

    def index_harse(self, cont):
        soup = BeautifulSoup(cont, 'html.parser')
        urls = self._get_urls(soup)
        return urls
