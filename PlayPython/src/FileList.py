'''
Created on 2014/6/6

@author: Administrator
'''
import os

# for path, folder, filelist in os.walk('E:\\tmp'):
#     for filename in filelist:
#         print os.path.join(path, filename)

for x in os.walk('E:\\tmp'):
    print x
    