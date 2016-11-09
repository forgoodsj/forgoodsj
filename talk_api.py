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
        recontent = (code,j['text'],j['url'])
    elif code == 302000:
        recontent= []
        num = 0
        for n in j['list']:
            recontent.append[(n['article'],'',n['icon'],n['detailurl'])]
            num = num + 1
        return (code,recontent,n)
    elif code == 308000:
        recontent = (code,j['text'],j['list'][0]['name'],j['list'][0]['info'],j['list'][0]['icon'],j['list'][0]['detailurl'])
    else:
        recontent = u'呆呆还不知道这是什么哎'
    return recontent


