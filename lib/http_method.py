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


info_msg = """do post:
url:
    %s
params:
    %s
"""
            
error_msg = """do post error:
%r
"""

def post(url,*args,**kwargs):
    """:
        1.请求参数:字典类型参数；
        2.请求url；
        3.成功返回请求字典，失败返回元组(True/False,errors information)。
    """
    dparams = {}
    for d in args:
        dparams.update(d)
    dparams.update(dict(kwargs))
        
    logger.info(info_msg,url,dparams)
    
    params = urllib.urlencode(dparams)
    try:
        charset = dparams.get("charset","utf-8")
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "charset":charset}
        if not url:
            return False,"请求地址不能为：%s" % str(url)
        request = urllib2.Request(url,params,headers)
        response = urllib2.urlopen(request, timeout=TIMEOUT)
        
        if response.code != 200:
            msg = "返回失败，错误代码:%s" % response.code 
            logger.error(error_msg,msg)
            return False,msg
        response_data = response.read()
        
        logger.info("response_data:%r",response_data)
        
        response_data = response_data.decode(charset)
        response_data = simplejson.loads(response_data)
        return True,response_data
    except Exception,err:
        msg = "http请求异常：%s" % str(err)
        logger.exception(error_msg,msg)
        return False,msg
    
    
def post_json(url,*args,**kwargs):
    """:
        1.请求参数:字典类型参数；
        2.请求url；
        3.成功返回请求字典，失败返回元组(True/False,errors information)。
    """
    dparams = {}
    for d in args:
        dparams.update(d)
    dparams.update(dict(kwargs))
        
    logger.info(info_msg,url,dparams)
    
#     params = urllib.urlencode(dparams)
    try:
        charset = dparams.get("charset","utf-8")
        headers = {"Content-type": "text/html",
                   "charset":charset}
        if not url:
            return False,"请求地址不能为：%s" % str(url)
        params = simplejson.dumps(dparams, ensure_ascii=False).encode("utf-8")
        request = urllib2.Request(url,params,headers)
        response = urllib2.urlopen(request, timeout=TIMEOUT)
        
        if response.code != 200:
            msg = "返回失败，错误代码:%s" % response.code 
            logger.error(error_msg,msg)
            return False,msg
        response_data = response.read()
        print response_data
        logger.info("response_data:%r",response_data)
        response_data = response_data[response_data.index("{")::]
        print response_data
#         response_data = response_data.decode(charset)
#         response_data = simplejson.loads(response_data)
        return True,response_data
    except Exception,err:
        msg = "http请求异常：%s" % str(err)
        logger.exception(error_msg,msg)
        return False,msg

# url='http://192.168.1.240:9000/ticket/v2.0/normalSellAgentTk.html'
# url='http://127.0.0.1:8081/gate/ticket/v2.0/normalSellAgentTk.html'
# params = {'ticket_ids':'6653683','user_id':82266}
#{u'data': [{u'code': u'4185132535267', u'sell_succeeded_at': u'2016-10-25 13:56:00', u'ticket_id': u'6653557'}], u'error_code': u'', u'success': True}
# url='http://192.168.1.240:9000/ticket/v2.0/returnAgentTk.html'

# params = {"sell_channel":"web","open_id":"82266","sell_use_id":82266,"back_apply_id":'1477548024588604',"is_all_refund":0,"back_fail_code":"test"}
url='http://127.0.0.1:8082/gz/ministry/query.html'
# url='http://127.0.0.1:8082/gz/ministry/sale.html'
params = {"publicrequest":{"requestid":"7828"},"body":{"orderno":"test","netticketid":""}}
state,data = post_json(url,params)

url = 'http://gate.cdqcp.net/'

def getAllCitys():
    url = '/ticket/v1.0/getAllCitys.html'
    state,data = post_json(url,params)

def query_shift():
    params = {}
