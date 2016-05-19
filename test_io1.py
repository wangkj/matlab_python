#!/usr/bin/env python
#coding=utf-8
import sys

t = open('sis001.txt','r')
print t.read()
text = t.read()
words = text.split()
wordcount = len(words)
print 'Wordcount:', wordcount
