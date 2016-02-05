#encoding:utf-8
'''
suds 发送短信
'''
import sys, getopt
from suds.client import Client
'''地址'''
URL = 'http://211.147.239.62/Service/WebService.asmx?wsdl'
'''用户名'''
ACCOUNT = 'cdbst@cdbst'
'''密码'''
PASSWORD = 'BST88:.xu'
'''系统编码'''
DECODE = 'UTF-8'

ws = Client(URL).service

def send(mobile,content):
    '''发送短信'''
    mobile = mobile.strip()
    if mobile.isdigit() and len(mobile)==11:
        parms = dict(account=ACCOUNT,password=PASSWORD,mobile=mobile,content=content)
        r = ws.PostSingle(**parms)
        if r==0:
            print u'%s 发送成功'%mobile
        else:
            print u'%s 发送失败'%mobile
    else:
        print '号码格式错误：%s'%mobile

def getMobiles(input_file):
    '''获取电话号码'''
    f = open(input_file)
    for line in f:
        yield line

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "f:c:p:")
    input_file = ''
    content = ''
    phone = ''
    for op, value in opts:
        if op == "-f":
            input_file = value
        elif op == "-c":
            content = value
        elif op == "-p":
            phone = value
    
    if input_file and content:
        content = content.decode(DECODE)
        for line in getMobiles(input_file):
            send(line,content)
                
    elif phone and content:
        content = content.decode(DECODE)
        phone = phone.decode(DECODE)
        send(phone,content)
    else:
        print '参数错误'

    

