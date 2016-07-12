from django.test import TestCase

# Create your tests here.
import time
ISOTIMEFORMAT='%Y-%m-%d %X'
now_time = time.strftime(ISOTIMEFORMAT, time.localtime())

def uid_add(uid_add):
    uid_add = "A0000045975E02"
    conn = MySQLdb.connect(host=qmdc_db.host,
                           port=qmdc_db.port,
                           user=qmdc_db.user,
                           passwd=qmdc_db.passwd,
                           db=qmdc_db.db,
                           charset=qmdc_db.charset)
    cursor = conn.cursor()
    add_sql = "INSERT INTO `signin_biz_acl_uid` (`created_time`, `updated_time`, `remarked_time`, `actions`, `updated_by`, `remarked_by`, `remarks`,`uid`) VALUES ('" + now_time + "', '" + now_time + "', '" + now_time + "', 7, 'script', 'script', '','" + uid_add + "');"
    cursor.execute(add_sql)
    add_data = cursor.fetchall()
    conn.commit()
    conn.close()
    print add_data