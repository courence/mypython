#encoding:utf-8
'''
配置信息
Created on Feb 16, 2016
@author: jh
'''

'''加载根路径'''
import sys, os
root = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root)


if __name__ == '__main__':
    print root
