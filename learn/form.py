# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget


#注册表单
class GetCodeForm(forms.Form):
#     mobile = forms.CharField()  
#     environment = forms.CharField()
    mobile = forms.CharField(max_length=11,label="mobile",widget=forms.TextInput(attrs={'class':'special','id':'mobile'}),error_messages={'required':u'手机号不能为空!'})
    environment_CHOICES=(
    ('test','test'),
    ('sim','sim/online')
    )
    environment = forms.ChoiceField(widget=forms.RadioSelect,choices=environment_CHOICES,label="environment",error_messages={'required': u'请选择环境!'})