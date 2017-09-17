#coding=utf-8


print "我爱中国"

import re

# 正则匹配,只从开始位置匹配，匹配不到返回 None
print re.match("www","www.baidu.com",flags=0).group()


#正则匹配 匹配整个字符串
print re.search("baidu","www.baidu.com",flags=0).span()


#检索和替换

print re.sub(r"\D","","0431-6845107")

