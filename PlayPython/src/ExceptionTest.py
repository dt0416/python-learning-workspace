'''
Created on 2014/6/6

@author: Administrator
'''
try:
    open('nofile.txt')
except Exception as ex:
    print ex
    