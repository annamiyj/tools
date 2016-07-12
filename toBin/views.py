#-*- coding:utf-8 –*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.

def toBin(request):
    # num10 = '894545678'
    logicbbit_enum = ['动态直减', 'OTA受限wrapper的报价', '可用星券', '可返星券','团队价',
                      '移动端2015情人节活动标志','WEB端2015情人节活动标志','签到超返','春节红包(又名签到红包)','前台拉新','车车券打包价',
                      '签到返现(含前台拉新)热门城市','电影票代金券','团购周边红包五折大促','周边红包五折大促现付','周边红包五折大促预付直减','周边红包五折大促预付后返',
                      '连锁酒店单体报价合并到集团售卖','返现价格转红包(裸价)','周边红包端午大促','周边五折老用户','团购直减转红包','非裸卖价格展示','周边红包机火红包大促',
                      '包房机火折扣','当日机火全量用户','机票用户标识','火车票用户标识','周边红包新用户标识','unknow','unknow','unknow','超反超减','目的地地推用户',
                      '团购目的地地推周边大促可用x币','门票用户标识','团购周边大促授信用户','商旅用户标识','团购召回新用户','双旦活动','礼，含门票标签',
                      'QTA促销DRR','商旅用户保险打包价','受中央低价库指导价影响的报价(很牛逼的样子）','unknow','低价服务敏感度测试报价','闪住','unknow','unknow','qta提前预定优惠','unknow','unknow','unknow','unknow','unknow','unknow','unknow','unknow','unknow']
    num10 = request.GET['num']
    if num10.isdigit():
        num2 = bin((int(num10)))
    else:
        return render_to_response('toBin.html',{'abc':u'输入错误，请输入纯数字'})
    tmp = []
    numtuple = []
    numtuple1 = []
    for i in num2:
        tmp.append(i)
    tmp.reverse()
    numlist = tmp[0:-2]
    for i, r in enumerate(numlist):
        numtuple.append({'No': i, 'Num': r})
    try:
        for j, z in enumerate(numtuple):
            z1 = z
            z1['enum'] = logicbbit_enum[j]
            numtuple1.append(z1)
        return render_to_response('toBin.html',{'data': numtuple1})
    except:
        return render_to_response('toBin.html', {'abc': u'输入错误，真的有这么长？'})

def toBin_home(request):
    return render(request, 'toBin.html')



