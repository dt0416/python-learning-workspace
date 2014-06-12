'''
Created on 2014/6/7

@author: Administrator
'''
from Student import StudentO

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age
        
hippo = Animal("Hippo", 18)
hippo.description()
stu = StudentO('Aaa', 20)
print stu.name