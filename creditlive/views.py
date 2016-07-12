#-*- coding:utf-8 –*-
from django.shortcuts import render
import MySQLdb
from zx_tools.environment import da_db
from django.http import HttpResponse
# Create your views here.

def creditlive_del(request):
    user_id = request.GET['user_id']
    conn = MySQLdb.connect(host=da_db.host,
                           port=da_db.port,
                           user=da_db.user,
                           passwd=da_db.passwd,
                           db=da_db.db,
                           charset=da_db.charset)
    cursor = conn.cursor()
    del_order = "DELETE FROM `datahotel_el`.`da_creditlive_order_info` WHERE  `user_id`='" + user_id +"'";
    del_user = "DELETE FROM `datahotel_el`.`da_creditlive_user_count` WHERE  `user_id`='" + user_id + "'";
    cursor.execute(del_user)
    cursor.execute(del_order)
    cursor.fetchall()
    conn.commit()
    conn.close()

    return HttpResponse(u"删除成功")

def creditlive(request):
    return render(request, 'creditlive.html')