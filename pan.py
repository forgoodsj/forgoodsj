#! /usr/bin/env python
#coding=utf-8
import requests
from bs4 import BeautifulSoup

def download_page(content):
    info = content.encode('utf-8')
    url ='http://www.wangpansou.cn/s.php?q='+ info
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
    data = requests.get(url, headers=headers).content
    
    return data

def pan(content):
    html = download_page(content)
    soup = BeautifulSoup(html)
    search_results = soup.find('div', attrs={'id': 'cse-search-result'})
    n = 1
    result_list = []
    picurl = ['https://mmbiz.qlogo.cn/mmbiz_jpg/w7XYZOGUbVEF44ibc9xULbXZO6pskUDibZaNtlJvxatpPMiaL9u96Dgbibsesae8704Tame1nMfVH4nARJbYJh2Wfw/0?wx_fmt=jpeg','https://mmbiz.qlogo.cn/mmbiz_png/w7XYZOGUbVEF44ibc9xULbXZO6pskUDibZQPb5gaPfWsZJJOiaw9Iib0Ng4JaiaHXibxtmDzzHAIxwicaicVVSrZIhwM2Q/0?wx_fmt=png']
    for search_result in search_results.find_all('div',attrs={'class': 'cse-search-result_content_item'}):
        if n <10:
            n = n+1
            result = []
            name = search_result.find('div', attrs={'class': 'cse-search-result_content_item_mid'}).getText().strip()
            url = search_result.a['href'] 
            result.append(name)
            result.append('')
            if n == 1:
                result.append(picurl[0])
            else:
                result.append(picurl[1])
            result.append(url)
            result_list.append(result)
        else:
            break
        result_list_num = [result_list, n]
    return result_list_num

#print pan(u'香肠派对')