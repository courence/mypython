#encoding:utf-8
'''
Created on Feb 15, 2016

@author: jh
'''
class Obj(object):
    '''创建对象'''
    def __init__(self,*args,**kwargs):
        for item in args:
            self.__dict__.update(item)
        if kwargs:
            self.__dict__.update(kwargs)