#encoding:utf-8
'''

Created on Jun 3, 2016
@author: jh
'''

import MySQLdb,time

class Mysqldb(object):
    def __init__(self,host,user,passwd,db,port=3306):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=3306)
        self.cur=self.conn.cursor()
        
    def select(self,sql,params=None):
        try:
            conn=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=3306)
            cur=conn.cursor()

            cur.execute(sql,params)
            result = cur.fetchall()
#             for item in result:
#                 print item
            conn.commit()
            cur.close()
            conn.close()
         
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    def select2(self,sql,params=None):
        self.cur.execute(sql,params)
        result = self.cur.fetchall()
        
if __name__ == '__main__':
    db = Mysqldb('192.168.1.214','root','server_VM14.DB','tmp_qzj')
    sql = "select now()"
    t1 = time.time()
    for i in range(5000):
        db.select2(sql)
    t2 = time.time()
    print t2-t1
