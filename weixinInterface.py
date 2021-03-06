# _*_ coding: utf-8 _*_
#https://zhuanlan.zhihu.com/p/22441695
import hashlib
import web
import lxml
import time
import datetime
import os
import json
import urllib
from lxml import etree
import imgtest
import talk_api
import loc
import movietop10
import pan


class WeixinInterface:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        
    def GET(self):
        #获取输入参数
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        #自己的token
        token = "weixin"
        #字典序排序
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list)
        hashcode = sha1.hexdigest()
        #sha1加密算法
        
        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
        
        
    def POST(self):
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        userid = fromUser[0:14]
        timeNow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        location = []
        if msgType == 'text':
            content = xml.find("Content").text
        elif msgType == 'voice':
            content = xml.find("Recognition").text
        elif msgType == 'image':
            try:
                media_id = xml.find("MediaId").text
                return self.render.reply_image(fromUser, toUser, int(time.time()), media_id)
            except:
                return self.render.reply_text(fromUser, toUser, int(time.time()),  '呆呆看不懂图片哎')
        elif msgType == 'location':
            Location_X = xml.find("Location_X").text
            Location_Y = xml.find("Location_Y").text
            Label = xml.find("Label").text
            reply = u'你的地理位置是\n纬度:%s;经度:%s;位置:%s'%(Location_X,Location_Y,Label)
            return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
            

        if content == u"今天是什么日子":
            d1 = datetime.datetime.now()
            d2 = datetime.datetime(2013,11,4)
            timedelta = str(d1 - d2)[:4]
            if timeNow[8:10] =="04":
                if timeNow[5:10] == "11-04":
                    year = int(timeNow[0:4]) - 2013
                    reply = u'哇！今天是叔叔和baby的%s周年纪念日~好棒呀！我们要白头偕老~'%year
                    return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
                else:
                    reply = u'哇！今天是叔叔和baby的纪念日,在一起%s天啦~一定要好好庆祝呀~'%timedelta
                    return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
            elif timeNow[5:10]=="05-28":
                reply = u'baby~生日快乐~呆呆和叔叔永远爱你~baby和叔叔在一起%s天啦~'%timedelta
                return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
            else:
                #key = 'd2ddb6c8b6d84b4c8c278868ec74fcae'
                #api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
                #info = content.encode('utf-8')
                #url = api + info
                #page = urllib.urlopen(url)
                #html = page.read()
                #dic_json = json.loads(html)
                #reply_content = dic_json['text']                    
                info = content.encode('utf-8')
                msg = talk_api.talk(info,userid)
                timereply = u'   哇赛！今天是叔叔和baby在一起的第%s天啦~~'%timedelta
                timereply1 =timereply.encode('utf-8')
                reply = msg + timereply1
                return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
                    
        elif content == u"我的id":
            return self.render.reply_text(fromUser,toUser,int(time.time()),fromUser)
            
        elif content[0:3] == u"百度云":
            info = content[3:]
            msg = pan.pan(info)
            return self.render.reply_news(fromUser,toUser,int(time.time()),msg[0],msg[1])
            
                            
        elif u'电影' in content:
            msg = movietop10.parse_html()
            return self.render.reply_news(fromUser,toUser,int(time.time()),msg[0],msg[1])
        
        else: 
            info = content.encode('utf-8')
            msg = talk_api.talk(info,userid)
            if isinstance(msg,str):
                return self.render.reply_text(fromUser,toUser,int(time.time()),msg)
            elif isinstance(msg,tuple):                   
                if msg[0] == 200000:
                    
                    return self.render.reply_onenew(fromUser,toUser,int(time.time()),content,msg[1],'',msg[2])
                elif msg[0] == 302000:                        
                    return self.render.reply_news(fromUser,toUser,int(time.time()),msg[1],msg[2])                        
                elif msg[0] == 308000:
                    return self.render.reply_news(fromUser,toUser,int(time.time()),msg[1],msg[2])   
                                        
            else:
                return self.render.reply_text(fromUser,toUser,int(time.time()),u'呆呆出问题了')
        
        
                   
        '''              
            
        elif msgType == 'voice': 
            content = xml.find("Recognition").text          
            info = content.encode('utf-8')
            msg = talk_api.talk(info,userid)
            if content == u"今天是什么日子":
                d1 = datetime.datetime.now()
                d2 = datetime.datetime(2013,11,4)
                timedelta = str(d1 - d2)[:4]
                if timeNow[8:10] =="04":
                    if timeNow[5:10] == "11-04":
                        year = int(timeNow[0:4]) - 2013
                        reply = u'哇！今天是叔叔和baby的%s周年纪念日~好棒呀！我们要白头偕老~'%year
                        return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
                    else:
                        reply = u'哇！今天是叔叔和baby的纪念日,在一起%s天啦~一定要好好庆祝呀~'%timedelta
                        return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
                elif timeNow[5:10]=="05-28":
                    reply = u'baby~生日快乐~呆呆和叔叔永远爱你~baby和叔叔在一起%s天啦~'%timedelta
                    return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
                else:
                    info = content.encode('utf-8')
                    msg = talk_api.talk(info,userid)
                    timereply = u'   哇赛！今天是叔叔和baby在一起的第%s天啦~~'%timedelta
                    timereply1 =timereply.encode('utf-8')
                    reply = msg + timereply1
                    return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
                                
            elif content == u"我的id":
                return self.render.reply_text(fromUser,toUser,int(time.time()),fromUser)
            
            elif content[0:3] == u"百度云":
                info = content[3:]
                msg = pan.pan(info)
                #return self.render.reply_news(fromUser,toUser,int(time.time()),msg,10)
                return self.render.reply_text(fromUser,toUser,int(time.time()),msg[0],msg[1])
            
            elif u'电影' in content:
                msg = movietop10.parse_html()
                return self.render.reply_news(fromUser,toUser,int(time.time()),msg[0],msg[1])
            
            else:                            
                info = content.encode('utf-8')
                msg = talk_api.talk(info,userid)
                if isinstance(msg,str):
                    return self.render.reply_text(fromUser,toUser,int(time.time()),msg)
                elif isinstance(msg,tuple):                               
                    if msg[0] == 200000:
                        return self.render.reply_onenew(fromUser,toUser,int(time.time()),content,msg[1],'',msg[2])
                    elif msg[0] == 302000:                        
                        return self.render.reply_news(fromUser,toUser,int(time.time()),msg[1],msg[2])
                    elif msg[0] == 308000:
                        return self.render.reply_news(fromUser,toUser,int(time.time()),msg[1],msg[2])   
                                
                                
                else:
                    return self.render.reply_text(fromUser,toUser,int(time.time()),u'呆呆出问题了')
            
        '''                   
        
        
        
           
       
    
            
        
        
        
              



   
                                      
                                     
                        
        
