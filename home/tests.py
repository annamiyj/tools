#-*- coding:utf-8 –*-
import urllib2
from sgmllib import SGMLParser

def identity_search():
    content = urllib2.urlopen('http://identity.daoapp.io/?num=5&min=20').read()
    listname = ListName()
    listname.feed(content)
    tmp = []
    users = []
    for item in listname.name:
        tmp.append(item)
    tmp1 = [(tmp[i], tmp[i + 1], tmp[i + 2], tmp[i + 3], tmp[i + 4], tmp[i + 5]) for i in range(len(tmp))[::6]]
    for r in tmp1:
        users.append({'name': r[0], 'id': r[1], 'birthday': r[2], 'age': r[3], 'sex': r[4], 'address': r[5]})

    print str(users).decode('string_escape')
    # for i in range(0, len(test)):
    #     if i%5 == 0:
    #         print '\n'
    #     else:
    #         print test[i]





class ListName(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_td = ""
        self.name = []
    def start_td(self, attds):
        self.is_td = 1
    def end_td(self):
        self.is_td = ""
    def handle_data(self, text):
        if self.is_td == 1:
            self.name.append(text)
identity_search()

