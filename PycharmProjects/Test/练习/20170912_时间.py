#coding=utf-8

print "我是中国人"

import time;

import calendar

ti = time.time()
print "当前时间戳",ti

ti1 = time.localtime(ti)
print "本地时间为：",ti1

ti2 = time.asctime(ti1)
print "格式化时间",ti2


# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))


print time.timezone

##########calendar


print calendar.month(2017,9)


