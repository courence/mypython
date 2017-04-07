#encoding:utf-8
'''
Created on Dec 2, 2016

@author: jh
'''
from pymongo import MongoClient
import random
import time,threading

client = MongoClient() 
client = MongoClient("localhost", 27017)
client = MongoClient("mongodb://localhost:27017/")

db = client.test
user = db.user

charts = list('abcdefghijklmnopqrstuvwxyz')
def insert(n):
    tb = time.time()
    for i in xrange(9999):
        name = random.choice(charts)+random.choice(charts)+random.choice(charts)
        age = random.randint(1,100)
        sex = random.choice(['male','female'])
        user.insert({"name":name, "sex":sex,"age":age})
        print i
    te = time.time()
    print '线程%s结束：%s时间：%s'%(n,threading.activeCount(),te-tb)

if __name__=='__main__':
    threading.Thread(target=insert,args=(1,)).start()