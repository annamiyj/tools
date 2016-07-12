#-*- coding:utf-8 –*-
from django.shortcuts import render
import MySQLdb
from zx_tools.environment import qmdc_db
from django.http import HttpResponse

# Create your views here.

def credituser_select(request):
    user_id = request.GET['user_id']
    conn = MySQLdb.connect(host=qmdc_db.host,
                           port=qmdc_db.port,
                           user=qmdc_db.user,
                           passwd=qmdc_db.passwd,
                           db=qmdc_db.db,
                           charset=qmdc_db.charset)
    cursor = conn.cursor()
    select_sql = "select user_type from credit_user_info where user_id = '" + user_id + "' or user_name = '" + user_id + "'";
    cursor.execute(select_sql)
    select = cursor.fetchall()
    conn.commit()
    conn.close()

    select_result = "账号身份是：" + credituser_enum(select)
    return HttpResponse(select_result)

def credituser_update(request):
    num = request.GET['select']
    user_id = request.GET['user_id']
    num = str(num)
    user_id = str(user_id)
    conn = MySQLdb.connect(host=qmdc_db.host,
                           port=qmdc_db.port,
                           user=qmdc_db.user,
                           passwd=qmdc_db.passwd,
                           db=qmdc_db.db,
                           charset=qmdc_db.charset)
    cursor = conn.cursor()
    update_sql = "update credit_user_info set user_type = '" + num + "' where user_id = '" + user_id + "' or user_name = '" + user_id + "'";
    cursor.execute(update_sql)
    conn.commit()

    cursor = conn.cursor()
    select_sql = "select user_type from credit_user_info where user_id = '" + user_id + "' or user_name = '" + user_id + "'";
    cursor.execute(select_sql)
    select = cursor.fetchall()
    conn.commit()
    conn.close()
    select_result = "修改成功、现在账号身份是：" + credituser_enum(select)
    return HttpResponse(select_result)

def credituser(request):
    return render(request, 'credituser.html')


def credituser_enum(Search_enum):
    if Search_enum == ():
        return "不在名单"
    enum = Search_enum[0][0]
    if enum == 1:
        return "授信用户"
    elif enum == 2:
        return "非授信用户"
    else:
        return "不在名单"