#!/usr/bin/python
# encoding:utf-8
'''
url访问相关
Created on Sep 30, 2014

@author: jh
'''
import urllib2,urllib 
from django.utils import simplejson
import logging
#过期时间
TIMEOUT = 30000

logger = logging



    

def post(url,charset,content_type,*args,**kwargs):
    '''
    发送post请求
    Parameters:
        url：访问地址
        charset：['utf-8','gbk']
        content_type:['text/plain','application/xml','application/json','text/html','application/rdf+xml']
    Returns:
         true,result
         false,error_msg
    '''
    dparams = {}
    for d in args:
        dparams.update(d)
    dparams.update(dict(kwargs))
    
    try:
        headers = {"Content-type": content_type,
                   "charset":charset}
        if not url:
            return False,"请求地址不能为：%s" % str(url)
        params = simplejson.dumps(dparams, ensure_ascii=False).encode(charset)
        request = urllib2.Request(url,params,headers)
        response = urllib2.urlopen(request, timeout=TIMEOUT)
        
        if response.code != 200:
            msg = "返回失败，错误代码:%s" % response.code 
            return False,msg
        response_data = response.read()
        print response_data
        response_data = response_data.decode(charset)
        return True,response_data
    
    except Exception,err:
        msg = "http请求异常：%s" % str(err)
        return False,msg

def post_json(url,*args,**kwargs):
    return post(url,'utf-8','application/json',*args,**kwargs)

def post_html(url,*args,**kwargs):
    return post(url,'utf-8','text/html',*args,**kwargs)
