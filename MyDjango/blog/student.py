'''
Created on 2014/6/9

@author: Administrator
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getMyName(self): # only have one parameter
        return "My Name is" + self.name