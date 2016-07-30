# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from .form import GetCodeForm
from .MySqlConn import MySqlConn
from django.http import HttpResponse
from django.template import RequestContext  

#接口形式的直接传参的
# def getcode_test(request, mobile):
#     
# #     mobile = request.GET['mobile']
#     mobile=int(mobile)
# 
#     conn = MySQLdb.connect(host='jxq-off-ku-qa00.dns.ganji.com',
#                            port=3410,
#                            user='yanjing2',
#                            passwd='f884a21',
#                            db='jianzhi_crm',)
#     # conn=MySQLdb.connect(host="l-hoteldb3.h.beta.cn0.qunar.com",port=3306,user="hotelbeta",passwd="ikHhsdgndBjdslHSdsDew",db="hotel",charset='utf8')
#     cursor = conn.cursor()
#     select_sql1 = "select a.phone,a.content,FROM_UNIXTIME(a.send_time) from jianzhi_crm.sms_send_log a where a.phone="+str(mobile)+" and a.service_id =106 order by a.send_time desc limit 1"
#     cursor.execute(select_sql1)
#     result=cursor.fetchall()
#     phone=mobile
#     code=result[0][1][-7:-1]
#     time=result[0][2]
#     cursor.close()
#     conn.close()
#     return render_to_response('getcodej.html', locals())
#
#接口形式的直接传参的
# def getcode_online(request, mobile):
#     
# #     mobile = request.GET['mobile']
#     mobile=int(mobile)
# 
#     conn = MySQLdb.connect(host='g1-off-ku-real.dns.doumi.com',
#                            port=3936,
#                            user='yanjing',
#                            passwd='14207114',
#                            db='jianzhi_crm',)
#     # conn=MySQLdb.connect(host="l-hoteldb3.h.beta.cn0.qunar.com",port=3306,user="hotelbeta",passwd="ikHhsdgndBjdslHSdsDew",db="hotel",charset='utf8')
#     cursor = conn.cursor()
#     select_sql1 = "select a.phone,a.content,FROM_UNIXTIME(a.send_time) from jianzhi_crm.sms_send_log a where a.phone="+str(mobile)+" and a.service_id =106 order by a.send_time desc limit 1"
#     cursor.execute(select_sql1)
#     result=cursor.fetchall()
#     phone=mobile
#     code=result[0][1][-7:-1]
#     time=result[0][2]
#     cursor.close()
#     conn.close()
#     return render_to_response('getcodej.html', locals())
#


#django表单方法
def getcode(request):
    if request.method == 'POST':# 当提交表单时
        form = GetCodeForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            mobile=form.cleaned_data['mobile']
            environment=form.cleaned_data['environment']
            if environment in ['test','TEST','Test']:
                scheme=MySqlConn().mysqlconntest("select a.phone,a.content,FROM_UNIXTIME(a.send_time) from jianzhi_crm.sms_send_log a where a.phone="+str(mobile)+" and a.service_id =106 order by a.send_time desc limit 1","test")
                #无结果时
                try:
                    code=scheme[0][1][-7:-1]
                    sendtime=scheme[0][2]
                    time=sendtime.strftime("%Y-%m-%d %H:%M:%S")
    #                 return HttpResponse('验证码：'+code+'     发送时间：'+str(time))
                    return render_to_response('formindex.html', locals(), context_instance=RequestContext(request))
                except IndexError:
                    message="未查询到验证码！"
                    return render_to_response('formindex.html', locals(), context_instance=RequestContext(request))
            elif environment in ['sim','SIM','Sim','online','ONLINE','Online','OnLine']:
                scheme=MySqlConn().mysqlconntest("select a.phone,a.content,FROM_UNIXTIME(a.send_time) from jianzhi_crm.sms_send_log a where a.phone="+"'"+str(mobile)+"'"+" and a.service_id =106 order by a.send_time desc limit 1","sim")
                try:
                    code=scheme[0][1][-7:-1]
                    sendtime=scheme[0][2]
                    time=sendtime.strftime("%Y-%m-%d %H:%M:%S")
    #                 return HttpResponse('验证码：'+code+'     发送时间：'+str(time))
                    return render_to_response('formindex.html', locals(), context_instance=RequestContext(request))
                except IndexError:
                    message="未查询到验证码！"
                    return render_to_response('formindex.html', locals(), context_instance=RequestContext(request))
    else:
        form=GetCodeForm()
    return render(request, 'formindex.html',{'form':form})


def index(request):
    return render_to_response('getcode.html')

#简单表单方法
def getverifycode(request):
    mobile = request.GET['mobile']
    environment = request.GET['environment']
    if mobile.isdigit():
        if environment in ['test']:
            scheme=MySqlConn().mysqlconntest("select a.phone,a.content,FROM_UNIXTIME(a.send_time) from jianzhi_crm.sms_send_log a where a.phone="+"'"+str(mobile)+"'"+" and a.service_id=106 order by a.send_time desc limit 1", "test")
            # 无结果时
            try:
                code = scheme[0][1][-7:-1]
                sendtime = scheme[0][2]
                time = sendtime.strftime("%Y-%m-%d %H:%M:%S")
                return render_to_response('getcode.html', locals())
            except IndexError:
                message = "未查询到验证码！"
                return render_to_response('getcode.html', locals())
        elif environment in ['sim']:
            scheme=MySqlConn().mysqlconntest("select a.phone,a.content,FROM_UNIXTIME(a.send_time) from jianzhi_crm.sms_send_log a where a.phone="+"'"+str(mobile)+"'"+" and a.service_id=106 order by a.send_time desc limit 1", "sim")
            # 无结果时
            try:
                code = scheme[0][1][-7:-1]
                sendtime = scheme[0][2]
                time = sendtime.strftime("%Y-%m-%d %H:%M:%S")
                return render_to_response('getcode.html', locals())
            except IndexError:
                message = "未查询到验证码！"
                return render_to_response('getcode.html', locals())
    else:
        message = "手机号格式不正确！"
        return render_to_response('getcode.html', message)

def newphone(request):
    return render_to_response('newphone.html')
