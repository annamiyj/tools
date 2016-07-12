# -*- coding: utf-8 -*-
import MySQLdb
import os

conn=MySQLdb.connect(host="10.86.32.92",port=3317,user="wap_h_beta",passwd="Q08pYvhoq6jk",db="mhotelred",charset='utf8')
cursor = conn.cursor()

uid = raw_input ("请输入你帐户对应的手机号码:")

select_sql = "SELECT uid,actions from signin_biz_acl_uid where uid = '" + uid +"'"
insert_sql = "INSERT INTO `signin_biz_acl_uid` (`created_time`, `updated_time`, `remarked_time`, `actions`, `updated_by`, `remarked_by`, `remarks`,`uid`) VALUES ('2015-08-25 15:24:51', '2015-08-25 15:24:51', '2015-08-25 15:24:51', 7, 'script', 'script', '','" + uid + "');"
delete_sql = "delete from `signin_biz_acl_uid` where uid= '" + uid +"'"


action = raw_input ("请选择需要进行的操作：1、增加白名单，2、删除白名单")

if action.startswith('1',0):
	insert_tmp=cursor.execute(insert_sql)
	print "插入" + uid + "记录"  + str(insert_tmp) + "条"
elif action.startswith('2',0):
        delete_tmp=cursor.execute(delete_sql)
        print "删除" + uid + "记录" + str(delete_tmp) + "条"
else:
        print '未选择要进行的操作，退出'
conn.commit()        
conn.close()
