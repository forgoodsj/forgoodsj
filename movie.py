#! /usr/bin/env python
#coding=utf-8
#https://zhuanlan.zhihu.com/p/22494756?refer=python-excavator
import requests
import re
import json
import time
import urllib2

def douban_movie():
    douban_url = 'https://movie.douban.com/'
    douban_html = urllib2.urlopen(douban_url).read().decode("utf-8")
    #c = re.compile(r'<a onclick="moreurl.*?href="(.*?)"[\s\S]*?src="(.*?)" alt="(.*?)" [\s\S]*?class="subject-rate">(.*?)</span>', re.S)
    c = re.compile(r'href="https://movie.douban.com/subject/3025375/?from=(.......)', re.S)
    DOUBAN = re.findall(c, douban_html)
    return DOUBAN
     #电影url链接，电影宣传图片，电影标题，电影评分。
    '''
    piaofang_url = 'http://www.cbooo.cn/boxOffice/GetHourBoxOffice?d=%s'%str(time.time()).split('.')[0]
    piaofang_json = requests.get(piaofang_url).text
    PIAOFANG = json.loads(piaofang_json)['data2']
    PIAOFANGS = []
    for piaofang in PIAOFANG:
        PIAOFANGS.append((piaofang['MovieName'], float(piaofang['sumBoxOffice'])))
    PIAOFANGS = sorted(PIAOFANGS, key=lambda x: x[1], reverse=True)#根据第二项反向（从大到小）排列

    INFO = []
    for piao in PIAOFANGS:
        piaofang_name = piao[0]
        for douban in DOUBAN:
            douban = list(douban)
            douban_name = douban[2]
            if piaofang_name == douban_name:
                douban.append(str("%.3f"%(piao[1]/10000.0)))
                #加入票房
                INFOS.append(douban)
                break
    totol_num = len(INFOS)
    if total_num>10:
        num = 10
    else:
        num = totle_num
            
    return (INFO[:num-1], num)
    '''
    
a = douban_movie()
print a
