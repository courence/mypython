#encoding:utf-8
'''
处理输入参数
Created on Feb 15, 2016

@author: jh
'''
import os, sys, getopt

from lib.obj import Obj

'''参数类型'''
ParamType = Obj(IFILE = 'infile',OFILE = 'outfile',DIGIT = 'digit',STRING = 'string')

class InputParam(object):
    '''获取输入参数'''
    def __init__(self,sourceParams):
        self.sourceParams = sourceParams #原始参数
        self.params = {}  #返回参数
        self.msg = ""  #错误形象
        self.isValid = True #参数处理结果
        
        self.helpMsg = "-----------------------参数格式----------------------\n"
        
        self.shortopts = 'h'
        self.longopts = ['help']
        
        '''解析传入参数'''
        self.__parseParams()
        
        try:
            '''解析命令参数'''
            self.opts, self.args = getopt.getopt(sys.argv[1:], self.shortopts,self.longopts)
            '''生成返回参数'''
            self.__createParams()
        except:
            self.__setMsg(self.helpMsg)
        
        '''显示帮助信息'''
        if 'h' in self.params or 'help' in self.params:
            self.__setMsg(self.helpMsg)
            
    def __parseParams(self):
        '''解析传入参数'''
        for k,v in self.sourceParams.items():
            self.__getopts(k,v)
            self.__helpMsg(k,v)
            
    def __getopts(self,k,v):
        if len(k)==1:
            self.shortopts += k
            if v:self.shortopts += ':'
        else:
            t = ''
            if v:t = "="
            self.longopts.append(k+t)
    
    def __helpMsg(self,k,v):
        t = '='
        if not v: 
            v = ""
            t = ""
        if len(k)==1:
            self.helpMsg += "-%s %s\n"%(k,v)
        else:
            self.helpMsg += "--%s%s%s\n"%(k,t,v)
    
    def __createParams(self):
        '''生成返回参数'''
        for op, value in self.opts:
            if len(op)==2 and '-'==op[0]:
                key = op[1]
            elif len(op)>2 and '--'==op[0:2]:
                key = op[2::]
            
            if self.__valid(op, value, self.sourceParams.get(key)):
                self.params[key] = value
            
                
    def __valid(self,op,value,paramtype):
        '''输入参数验证'''
        if paramtype==ParamType.IFILE:
            if not os.path.exists(value):
                self.__setMsg("%s %s 文件不存在 \n"%(op,value))
        if paramtype==ParamType.OFILE:
            if os.path.exists(value):
                self.__setMsg("%s %s 文件已存在 \n"%(op,value))
        if paramtype==ParamType.DIGIT:
            if not value.isdigit():
                self.__setMsg("%s %s 参数需为数字 \n"%(op,value))
        return self.msg==''
            
    def __setMsg(self,msg):
        self.msg += msg
        self.isValid = False

    
if __name__ == '__main__':
    '''例子'''
    inputParam = InputParam({"i":ParamType.IFILE,'o':ParamType.OFILE,
                             'digit':ParamType.DIGIT,'s':ParamType.STRING})
    if inputParam.isValid:
        print inputParam.params
    else:
        print inputParam.msg