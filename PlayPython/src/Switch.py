'''
Created on 2014/6/4

@author: Administrator
'''
score = int(input('please input'))
level = score // 10
print {
    10 : lambda : 'Perfect',
    9  : lambda : 'A',
    8  : lambda : 'B',
    7  : lambda : 'C',
    6  : lambda : 'D'
}.get(level, lambda: 'E')()