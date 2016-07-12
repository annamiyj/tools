from django.test import TestCase

# Create your tests here.
import os

def read(self):
    fr = open(r'G:\zx\python\zx_tool\home\static\note.txt','r')
    note_read = ''
    for line in fr:
        note_read += line
    print note_read


def write(note):
    fw = open('../templates/note.txt', 'a+')
    note1 = '\n' + note
    fw.write(note1)
    fw.close()
    read(note1)

note = '123455'
write(note)