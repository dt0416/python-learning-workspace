'''
Created on 2014/6/3

@author: Administrator
'''
def fun111(a, b):
    print a, b

def funMul(x, *args, **kwargs):
    print args
    print type(args)
    print kwargs
    print type(kwargs)
    
g = lambda x, y: x*y
g1 = lambda : 1+1
dic = {'a':123, 'b':456}
fun111(**dic)
funMul(1, 2, 3, 4, 5, a=1, args=2)
print g(1,2)
print g1(1)
