#! /usr/bin/env python
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import codecs

url ='https://movie.douban.com/nowplaying/shanghai/'

def download_page():
    url ='https://movie.douban.com/nowplaying/shanghai/'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
    data = requests.get(url, headers=headers).content
    
    return data

def parse_html():
    html = download_page()
    soup = BeautifulSoup(html)
    
    movie_now = soup.find('div', attrs={'id': 'nowplaying'})
    movie_modbd = movie_now.find('div', attrs={'class': 'mod-bd'})
    movie_list_soup = movie_modbd.find('ul', attrs={'class': 'lists'})
    movie_list = []    
    n = 0
    for movie_li in movie_list_soup.find_all('li',attrs={'class': 'list-item'}):
        try:
            if n <10:            
                movie =[]
                movie_name = movie_li.img['alt']          
                movie_score = movie_li.find('span', attrs={'class': 'subject-rate'}).getText()
                #movie_director = movie_li.li['data-director']
                #movie_actors = movie_li.li['data-actors']
                movie_url = movie_li.a['href']
                movie_picurl = movie_li.img['src']
                #movie.append(movie_name+u'    评分:'+movie_score,u'评分:'+movie_score,movie_picurl,movie_url)
                #movie = {'movie_name':movie_name,'movie_score':movie_score,'movie_url':movie_url,'movie_picurl':movie_picurl}
                movie.append(movie_name+u'    评分:'+movie_score)
                movie.append(movie_score)
                movie.append(movie_picurl)
                movie.append(movie_url)
                movie_list.append(movie)
                n = n+1
        except:
            pass
        
    movie_list.sort(key=lambda x:float(x[1]),reverse=True)
    movie_list_num = [movie_list, n]
    return movie_list


#print parse_html()
   