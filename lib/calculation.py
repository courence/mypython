#encoding:utf-8
'''
计算相关
Created on Feb 22, 2016
@author: jh
'''

from decimal import Decimal
def dictsum(lst):
    '''
    字典类型列表求和 输入字典列表，返回求和字典
    '''
    result = {}
    for item in lst:
        for k,v in item.items():
            '''求和>数字>字符>空'''
            t = result.get(k)
            if iscomputable(v):
                if iscomputable(t):
                    t += v
                else:
                    t = v
            elif not t:
                t = v
                
            result[k] = t
    return result

def iscomputable(n):
    '''参数是否可计算'''
    try:
        Decimal(n)
        return True
    except:
        return False

if __name__ == '__main__':
    result = [{'a':1},{'a':'b'},{'a':2.5}]
    print dictsum(result)
