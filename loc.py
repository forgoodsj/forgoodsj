#! /usr/bin/env python
#coding=utf-8
import requests
import json
global s
s = requests.session()

url1='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxf976343365df3ef0&secret=59a593ae219a578b6c325bce639e0a0b'
a = s.get(url1)
b = eval(a.text)
access_token = b['access_token']
def loc(openid):
    url = 'https://api.weixin.qq.com/cgi-bin/user/info/batchget?access_token=%s'%access_token
    da = {"openid": openid, "lang": "zh-CN"}
    data = json.dumps(da)
    r = s.post(url, data=data)
    j = eval(r.text)
    city = j['user_info_list'][0]['city']
    return city

#微信接口没有权限
    
    




    
