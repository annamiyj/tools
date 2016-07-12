from django.test import TestCase

# Create your tests here.
num10 = '50'
num2 = bin(int(num10))
tmp = []
numlist1 = []
enum= ['a', 'b', 'c', 'd','q','2','r']
for i in num2:
    tmp.append(i)
tmp.reverse()
numlist = tmp[0:-2]
enum1 = enum[0:len(numlist)]
for i, r in enumerate(numlist):
    numlist1.append({'No': i, 'Num': r})
z2 = []
for j,z in enumerate(numlist1):
    z1 = z
    z1['word'] = enum[j]
    z2.append(z1)
print z2

# for i,r in enumerate(users_tmp):
#     numlist1.append({'No.': i,'Num.':r[0],'qwe':r[1]})