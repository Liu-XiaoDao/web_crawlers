#! /usr/bin/python

import pynotify
import random
from time import sleep

fw = open('cet_6_vocab.txt','r')
vocab = fw.read()
vocab = vocab.split('\n')

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

i = random.randint(0,len(vocab)-1)
word_array = vocab[i].split(' ')
word = word_array.pop(0)
translate = '\n'.join(word_array)
sendmessage(word,translate)
