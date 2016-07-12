from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import MySQLdb
from zx_tools.environment import twell_db
import os
# Create your views here.


def nametoseq(request):

    name = request.GET['name']

    conn = MySQLdb.connect(host=twell_db.host,
                           port=twell_db.port,
                           user=twell_db.user,
                           passwd=twell_db.passwd,
                           db=twell_db.db,
                           charset=twell_db.charset)
    # conn=MySQLdb.connect(host="l-hoteldb3.h.beta.cn0.qunar.com",port=3306,user="hotelbeta",passwd="ikHhsdgndBjdslHSdsDew",db="hotel",charset='utf8')
    cursor = conn.cursor()
    select_sql1 = "select  native_name,hotel_seq from wrapper_transname where native_name like  '" + name + "%"  + "'  limit 5"
    cursor.execute(select_sql1)
    result=cursor.fetchall()
    result2 = []
    empty = ' ---         '
    for i in range(0,len(result)):
        for j in range(0,2):
           result1=result[i][j]
           result2.append(result1)
           result3=empty.join(result2)
        j=j+1
    conn.commit()
    conn.close()

    return HttpResponse(result3)


def seqtoname(request):

    seq = request.GET['seq']

    conn = MySQLdb.connect(host=twell_db.host,
                           port=twell_db.port,
                           user=twell_db.user,
                           passwd=twell_db.passwd,
                           db=twell_db.db,
                           charset=twell_db.charset)
    cursor = conn.cursor()
    select_sql = "select native_name from wrapper_transname where hotel_seq = '" + seq +"'"
    cursor.execute(select_sql)
    result=cursor.fetchall()
    conn.commit()
    conn.close()

    result_len = len(result)
    if result_len <> 0:
        return HttpResponse(result[0][0])
    else:
        return HttpResponse("beta is empty")

def hotelseq(request):
    return render(request, 'hotelseq.html')