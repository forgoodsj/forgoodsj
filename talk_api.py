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
        recontent = []
        '''
        num = len(j['list'])
        if num <= 10:
            for n in range(num-1):
                recontent.append((j['list'][n]['article'],j['list'][n]['source'],j['list'][n]['icon'],j['list'][n]['detailurl']))
            return (code , recontent, num)
        else:
            for n in range(9):
                recontent.append((j['list'][n]['article'],j['list'][n]['source'],j['list'][n]['icon'],j['list'][n]['detailurl']))
            return (code , recontent, 10)
        '''
        num = 0
        for n in j['list']:
            recontent.append((n['article'],n['source'],n['icon'],n['detailurl']))
            if num < 10:
                num = num + 1
            else:
                break
        return (code , recontent, num)
    elif code == 308000:
        #recontent = (code,j['text'],j['list'][0]['name'],j['list'][0]['info'],j['list'][0]['icon'],j['list'][0]['detailurl'])
        recontent = []
        num = 0
        picurl=['https://mmbiz.qlogo.cn/mmbiz_jpg/w7XYZOGUbVEE0zl6MWr1MZj695AtnK2GibSfY3O03ZdTtZrcCRCNFcl3eNOZ5PiabmC5fMJHECpw2IJvJzjrVZrA/0?wx_fmt=jpeg',
        'https://mmbiz.qlogo.cn/mmbiz_png/w7XYZOGUbVEE0zl6MWr1MZj695AtnK2GTRC5lsfAtOO0OoWtxVRhyibeSKnPNHcdng82iaa5RO7y8iaIaf6k7j6aA/0?wx_fmt=png',
        'https://mmbiz.qlogo.cn/mmbiz_png/w7XYZOGUbVEE0zl6MWr1MZj695AtnK2G4C5kDwt0TsUVItgpRCehXG8ZVMKokDGSNWC7tiagtGJNTRTicEO937zg/0?wx_fmt=png',
        'https://mmbiz.qlogo.cn/mmbiz_png/w7XYZOGUbVEE0zl6MWr1MZj695AtnK2GyZzgfvDZc2Pg4xEpJicT3Wt11XzveblXfOCQLASJ1IaphRzFSaHrpicg/0?wx_fmt=png',
        'https://mmbiz.qlogo.cn/mmbiz_png/w7XYZOGUbVEE0zl6MWr1MZj695AtnK2GlXlL8MASn2ibR2CJTCZBNpQXx17iaoIP3W3Gaha4uCTydZTQkGxRhiciaQ/0?wx_fmt=png',
        'https://mmbiz.qlogo.cn/mmbiz_png/w7XYZOGUbVEE0zl6MWr1MZj695AtnK2GmPPG7CbVxGOCicXibDzbBums59sfN9LbmTwicHZl2muzuvqcicmAR2BILQ/0?wx_fmt=png',
        'https://mmbiz.qlogo.cn/mmbiz_png/w7XYZOGUbVEE0zl6MWr1MZj695AtnK2GYA6IvaAN7zxTDRp2oeI96FN7bShg009ibf6mcwzXGb9QS6wFUwOGr8g/0?wx_fmt=png',
        'https://mmbiz.qlogo.cn/mmbiz_png/w7XYZOGUbVEE0zl6MWr1MZj695AtnK2GTzDL1Wjvg6jo8TgP9jEZibvOlJXBmgic7aaXnLvUTRibssS46nlhzQ28g/0?wx_fmt=png',
        'https://mmbiz.qlogo.cn/mmbiz_png/w7XYZOGUbVEE0zl6MWr1MZj695AtnK2Gibatuvu8ibL0AiaEwLlsCE9QaiayuGZELHfRa9Pk1P2axbXNDRd41ft5lg/0?wx_fmt=png',
        'https://mmbiz.qlogo.cn/mmbiz_png/w7XYZOGUbVEE0zl6MWr1MZj695AtnK2GLklDoiao3dpOalSUSRbolVcPl3svoF04Av7aZuZic9rCKIdGZmClct0A/0?wx_fmt=png']        
        for n in j['list']:
            if num < 10:
                recontent.append((n['name']+':'+n['info'],n['info'],picurl[num],n['detailurl']))
                num = num + 1
            else:
                break
        return (code , recontent, num)
        
    else:
        recontent = u'呆呆还不知道这是什么哎'
    return recontent



content = u'红烧肉'
userid = '123'
a =talk(content, userid)
print a


