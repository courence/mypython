#!/usr/bin/python
#encoding:utf-8
'''
编码转换
Created on Feb 16, 2016
@author: jh
'''
import config
from lib.inputparam import InputParam, ParamType
from lib import file


def tanscode(inputFile,outputFile,sourceCode,targetCode='utf-8'):
    '''编码转换'''
    lst = []
    for line in file.getline(inputFile):
        tstr = line.decode(sourceCode).encode(targetCode)
        lst.append(tstr)
        print tstr
    if outputFile:
        file.writefile(lst, outputFile)



if __name__ == '__main__':
    param = {'c':'gbk'}
    inputParam = InputParam({"i":ParamType.IFILE,'c':ParamType.STRING,'o':ParamType.OFILE})
    if inputParam.isValid:
        param.update(inputParam.params)
        inputFile = param.get('i')
        sourceCode = param.get('c')
        outputFile = param.get('o')
        if inputFile:
            tanscode(inputFile,outputFile,sourceCode)
        else:
            print inputParam.helpMsg
    else:
        print inputParam.msg