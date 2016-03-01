#encoding:utf-8
'''
字符串相关方法
Created on Feb 29, 2016
@author: jh
'''

class StringUtils(object):
    def join(self,lst,symbol=',',sformat='%s'):
        return symbol.join([sformat%item for item in lst])


stringUtils = StringUtils()

if __name__ == '__main__':
    pass
