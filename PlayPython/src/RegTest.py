'''
Created on 2014/6/4

@author: Administrator
'''
import re

str = '''python=123
pyyyyy=bbb
python=aaa
'''
pattern = r'python=(\w+)'
rPattern = re.compile(pattern)

print rPattern.findall(str)