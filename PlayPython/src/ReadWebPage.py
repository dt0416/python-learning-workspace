#coding:big5
'''
Created on 2014/6/5

@author: Administrator
取網站圖片
'''
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r"src=\"(.+.jpg)\".+width"
    imgRe = re.compile(reg)
    imgList = imgRe.findall(html)
    return imgList

def downJpg(imgList):
    x = 0
    for imgUrl in imgList:
        urllib.urlretrieve(imgUrl, '%s.jpg' % x)
        x += 1

html = getHtml('http://tw.yahoo.com')
# print html
imgList = getImg(html)
downJpg(imgList)
print 'done'