
#coding=utf-8

#全部引用
from yinyong import printName
#部分引用
import yinyong
#引用全部
from yinyong import *


#全部引用
yinyong.printName("聂超")

#部分引用
printName("孟玲洋")


#局部变量和全局变量

money = 2000

def addMoney():
    global money
    money += 1
    print money

print "金钱数量：",money

print "金钱数量",addMoney()

print "金钱的数量",money


#dir

import math

print dir(math)

print dir()








