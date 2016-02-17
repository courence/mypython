#encoding:utf-8
'''
文件相关操作
Created on Feb 5, 2016

@author: jh
'''
def getline(input_file):
    '''获取文件行数据'''
    f = open(input_file)
    for line in f:
        line = line.strip()
        if line:yield line
        
def writefile(lst,output_file,mode='w'):
    '''写文件'''
    f = open(output_file,mode)
    for line in lst:
        f.write(line+'\n')
    f.close()