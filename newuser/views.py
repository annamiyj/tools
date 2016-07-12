#-*- coding:utf-8 –*-
from django.shortcuts import render
# Create your views here.
import MySQLdb
import os
import time
from zx_tools.environment import qmdc_db
from django.http import HttpResponse



ISOTIMEFORMAT='%Y-%m-%d %X'
now_time = time.strftime(ISOTIMEFORMAT, time.localtime())


# uid部分
def newuser_uid(request):
    uid = request.GET['uid']
    uidSearch_Result = newuser_uid_search(uid)
    return HttpResponse(signin_enum(uidSearch_Result))

def newuser_uidadd(request):
    uid = request.GET['uid']
    uidSearch_Result = newuser_uid_search(uid)
    if len(uidSearch_Result) == 0:
        uid_add(uid)
    else:
        uid_update(uid)
    uidSearch_Result = newuser_uid_search(uid)
    uidAdd_result = ('uid:',uidSearch_Result[0][0],u' 添加成功')
    return HttpResponse(uidAdd_result)

def newuser_uiddel(request):
    uid = request.GET['uid']
    uidSearch_Result = newuser_uid_search(uid)
    if len(uidSearch_Result) == 0:
        return HttpResponse(u'uid: ' + uid + u'不在白名单，不需要删除')
    else:
        uid_del(uid)
        return HttpResponse(u'uid: ' + uid + u'删除成功')

# userid部分
def newuser_userid(request):
    userid = request.GET['userid']
    useridSearch_Result = userid_search(userid)
    return HttpResponse(signin_enum(useridSearch_Result))

def newuser_useridadd(request):
    userid = request.GET['userid']
    useridSearch_Result = userid_search(userid)
    if len(useridSearch_Result) == 0:
        userid_add(userid)
    else:
        userid_update(userid)
    useridSearch_Result = userid_search(userid)
    useridAdd_result = ('userid:',useridSearch_Result[0][0],u' 添加成功')
    return HttpResponse(useridAdd_result)

def newuser_useriddel(request):
    userid = request.GET['userid']
    useridSearch_Result = userid_search(userid)
    if len(useridSearch_Result) == 0:
        return HttpResponse(u'userid: ' + userid + u'不在白名单，不需要删除')
    else:
        userid_del(userid)
        return HttpResponse(u'userid: ' + userid + u'删除成功')


# 主页
def newuser(request):
    return render(request, 'newuser.html')



def newuser_uid_search(uid_search):

    # uid = request.GET['uid']
    # uid = '865072028127465'
    conn = MySQLdb.connect(host=qmdc_db.host,
                           port=qmdc_db.port,
                           user=qmdc_db.user,
                           passwd=qmdc_db.passwd,
                           db=qmdc_db.db,
                           charset=qmdc_db.charset)
    cursor = conn.cursor()
    select_sql = "SELECT uid,actions from signin_biz_acl_uid where uid = '" + uid_search + "'"
    cursor.execute(select_sql)
    select = cursor.fetchall()
    conn.commit()
    conn.close()
    return select



def uid_update(uid_update):
    conn = MySQLdb.connect(host=qmdc_db.host,
                           port=qmdc_db.port,
                           user=qmdc_db.user,
                           passwd=qmdc_db.passwd,
                           db=qmdc_db.db,
                           charset=qmdc_db.charset)
    cursor = conn.cursor()
    update_sql = "UPDATE `signin_biz_acl_uid` SET `actions`=7 WHERE uid = '" + uid_update + "';"
    cursor.execute(update_sql)
    update_data = cursor.fetchall()
    conn.commit()
    conn.close()
    return update_data

def uid_add(uid_add):
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
    return add_data

def uid_del(uid_del):
    conn = MySQLdb.connect(host=qmdc_db.host,
                           port=qmdc_db.port,
                           user=qmdc_db.user,
                           passwd=qmdc_db.passwd,
                           db=qmdc_db.db,
                           charset=qmdc_db.charset)
    cursor = conn.cursor()
    del_sql = "DELETE FROM `signin_biz_acl_uid` where `uid` = '" + uid_del + "';"
    cursor.execute(del_sql)
    del_data = cursor.fetchall()
    conn.commit()
    conn.close()
    return del_data

def userid_search(userid_search):

    # uid = request.GET['uid']
    # uid = '865072028127465'
    conn = MySQLdb.connect(host=qmdc_db.host,
                           port=qmdc_db.port,
                           user=qmdc_db.user,
                           passwd=qmdc_db.passwd,
                           db=qmdc_db.db,
                           charset=qmdc_db.charset)
    cursor = conn.cursor()
    select_sql = "SELECT user_id,actions from signin_biz_acl_userid where user_id = '" + userid_search + "'"
    cursor.execute(select_sql)
    select = cursor.fetchall()
    conn.commit()
    conn.close()
    return select



def userid_update(userid_update):
    conn = MySQLdb.connect(host=qmdc_db.host,
                           port=qmdc_db.port,
                           user=qmdc_db.user,
                           passwd=qmdc_db.passwd,
                           db=qmdc_db.db,
                           charset=qmdc_db.charset)
    cursor = conn.cursor()
    update_sql = "UPDATE `signin_biz_acl_userid` SET `actions`=7 WHERE user_id = '" + userid_update + "';"
    cursor.execute(update_sql)
    update_data = cursor.fetchall()
    conn.commit()
    conn.close()
    return update_data

def userid_add(userid_add):
    conn = MySQLdb.connect(host=qmdc_db.host,
                           port=qmdc_db.port,
                           user=qmdc_db.user,
                           passwd=qmdc_db.passwd,
                           db=qmdc_db.db,
                           charset=qmdc_db.charset)
    cursor = conn.cursor()
    add_sql = "INSERT INTO `signin_biz_acl_userid` (`created_time`, `updated_time`, `remarked_time`, `actions`, `updated_by`, `remarked_by`, `remarks`,`user_id`) VALUES ('" + now_time + "', '" + now_time + "', '" + now_time + "', 7, 'script', 'script', '','" + userid_add + "');"
    cursor.execute(add_sql)
    add_data = cursor.fetchall()
    conn.commit()
    conn.close()
    return add_data

def userid_del(userid_del):
    conn = MySQLdb.connect(host=qmdc_db.host,
                           port=qmdc_db.port,
                           user=qmdc_db.user,
                           passwd=qmdc_db.passwd,
                           db=qmdc_db.db,
                           charset=qmdc_db.charset)
    cursor = conn.cursor()
    del_sql = "DELETE FROM `signin_biz_acl_userid` where `user_id` = '" + userid_del + "';"
    cursor.execute(del_sql)
    del_data = cursor.fetchall()
    conn.commit()
    conn.close()
    return del_data

def signin_enum(Search_enum):
    # result_enum = raw_input("result:")
    if Search_enum == ():
        return "不在白名单"
    enum = Search_enum[0][1]
    if enum == 7:
        return "已在白名单、所有权限"
    elif enum == 3:
        return "已在白名单、只有查看报价权限"
    else:
        return "不在白名单"