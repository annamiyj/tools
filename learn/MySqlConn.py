# -*- coding=utf-8 -*-
import MySQLdb
from .ConFig import Testingenvironment

#连接数据库
class MySqlConn():
    def mysqlconntest(self,sqltxt,environment):
        
        #连接数据库
        #区分环境test
        if environment=='test' or environment=='TEST':
            host=Testingenvironment.host_test
            user=Testingenvironment.user_test
            passwd=Testingenvironment.passwd_test
            port=Testingenvironment.port_test
            db=Testingenvironment.dbcrm_test
        #sim
        elif environment=='sim' or environment=='SIM':
            host=Testingenvironment.host_sim
            user=Testingenvironment.user_sim
            passwd=Testingenvironment.passwd_sim
            port=Testingenvironment.port_sim
            db=Testingenvironment.dbcrm_sim
#         #online
#         elif environment=='online' or environment=='ONLINE':
#             host=Testingenvironment.host_online
#             user=Testingenvironment.user_online
#             passwd=Testingenvironment.passwd_online
#             port=Testingenvironment.port_online
#             db=Testingenvironment.db2_online
        try:
            conn=MySQLdb.connect(host=host,
                                 user=user,
                                 passwd=passwd,
                                 port=port,
                                 db=db)
            #使用连接对象获得一个cursor对象
            cursor=conn.cursor()
            #执行查询语句，获取time对应的数据
            cursor.execute(sqltxt)
            #接收全部返回结果+
            scheme=cursor.fetchall()
    #             print scheme
    #             print type(scheme)
    #             print scheme[0][1]
            cursor.close()
            conn.close()
            return scheme
        except MySQLdb.Error,e:
            #sim和online有两个库，3936和3935
            if e.args[0]==1142:
                port=Testingenvironment.port_sim2
                db=Testingenvironment.db2_sim2
                try:
                    conn=MySQLdb.connect(host=host,
                                     user=user,
                                     passwd=passwd,
                                     port=port,
                                     db=db)
                    #使用连接对象获得一个cursor对象
                    cursor=conn.cursor()
                    #执行查询语句，获取time对应的数据
                    cursor.execute(sqltxt)
                    #接收全部返回结果+
                    scheme=cursor.fetchall()
            #             print scheme
            #             print type(scheme)
            #             print scheme[0][1]
                    cursor.close()
                    conn.close()
                    return scheme
                except MySQLdb.Error,e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                    raise
            else:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                raise 
        
        
        
    
# xx=MySqlConn()
# xx.mysqlconntest("select a.id from jz_post a order by a.id desc limit 1 ","test")