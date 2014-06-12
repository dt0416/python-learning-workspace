'''
Created on 2014/6/6

@author: Administrator
'''
fo = open('test.txt', 'a')
list1 = ['abc\n', 'def\n', 'ghi']
fo.writelines(list1)
fo.close()