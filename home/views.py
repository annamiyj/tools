from django.shortcuts import render
from django.shortcuts import render_to_response
import urllib2
from sgmllib import SGMLParser
# Create your views here.
def home(request):
    return render(request, 'index.html')

def myjob(request):
    return render(request, 'myjob.html')

def note_read(request):
    fr = open(r'G:\zx\python\zx_tool\home\static\note.txt','r')
    note_r = ''
    for line in fr:
        note_r += line
    return render_to_response('myjob.html',{'note_read': note_r})



def note_write(request):
    tmp = request.GET['note_w']
    fw = open(r'G:\zx\python\zx_tool\home\static\note.txt', 'a+')
    note1 = '\n' + tmp
    fw.write(note1)
    fw.close()
    fr = open(r'G:\zx\python\zx_tool\home\static\note.txt', 'r')
    note_r = ''
    for line in fr:
        note_r += line
    return render_to_response('myjob.html', {'note_read': note_r})


def identity_home(request):
    return render(request, 'identity.html')

def identity_search(request):
	content = urllib2.urlopen('http://identity.daoapp.io/?num=20&min=15&max=60').read()
	listname = ListName()
	listname.feed(content)
	tmp = []
	users = []
	for item in listname.name:
		tmp.append(item)
	users_tmp = [(tmp[i], tmp[i + 1], tmp[i + 2], tmp[i + 3], tmp[i + 4], tmp[i + 5]) for i in range(len(tmp))[::6]]
	for r in users_tmp:
		users.append({'name': r[0], 'id': r[1], 'birthday': r[2], 'age': r[3], 'sex': r[4], 'address': r[5]})
	return render_to_response('identity.html',{'users': users})





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

