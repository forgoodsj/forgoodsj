#! /usr/bin/env python
#coding=utf-8
import requests
import json
global s
s = requests.session()


def talk(content, userid):
    url = 'http://www.tuling123.com/openapi/api'
    da = {"key": "897539c37d464a1ba5a22a5d4b17150d", "info": content, "userid": userid}
    data = json.dumps(da)
    r = s.post(url, data=data)
    j = eval(r.text)
    code = j['code']
    if code == 100000:
        recontent = j['text']
    elif code == 200000:
        recontent = j['text']+j['url']
    elif code == 302000:
        recontent = j['text']+j['list'][0]['article']+j['list'][0]['detailurl']
    elif code == 308000:
        recontent = j['text']+j['list'][0]['name']+j['list'][0]['detailurl']
    else:
        recontent = u'呆呆还不知道这是什么哎'
    return recontent

#content = '你好'
#msg = talk(content)
#info = msg.encode('utf-8')
#print info
