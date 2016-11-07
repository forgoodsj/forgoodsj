#! /usr/bin/env python
#coding=utf-8
import requests
import json
global s
s = requests.session()

def loc(openid):
    url = 'https://api.weixin.qq.com/cgi-bin/user/info/batchget?access_token=t6FgbziDST6e5mY3uM6ZBhBIQo8LhDUPROSsBacW17T'
    da = {"openid": openid, "lang": "zh-CN"}
    data = json.dumps(da)
    r = s.post(url, data=data)
    j = eval(r.text)
    city = j['user_info_list'][0]['city']
    return city
    
