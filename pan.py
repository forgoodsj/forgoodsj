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
    for search_result in search_results.find_all('div',attrs={'class': 'cse-search-result_content_item'}):
        if n <= 10:
            result = []
            name = search_result.find('div', attrs={'class': 'cse-search-result_content_item_mid'}).getText().strip()
            url = search_result.a['href'] 
            result.append(name)
            result.append('')
            result.append('')
            result.append(url)
            result_list.append(result)
            n = n+1
        else:
            break
    return result_list

print pan(u'速度与激情')