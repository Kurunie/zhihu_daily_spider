from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response
from spiderdata.models import Content
from spiderdata.spider_main import Spider
# Create your views here.


def result(request):
    r_url = 'https://daily.zhihu.com/'
    spider = Spider()
    spider.craw(r_url)
    res = Content.objects.all()
    data = []
    count = 0
    for r in res:
        data.append({})
        data[count]['url'] = r.urls
        data[count]['name'] = r.urlques
        data[count]['cont'] = []
        temp1 = r.author.split("@@")
        temp2 = r.urlans.split("@@")
        for i in range(len(temp1)):
            data[count]['cont'].append([temp1[i], temp2[i]])
        count += 1
    return render_to_response("result.html", {'data': data})