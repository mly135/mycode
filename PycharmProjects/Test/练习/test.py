#coding=utf-8

# 循环遍历,使用递归方式
def foreach(li):
    for i in li:
        if isinstance(i, list):
            foreach(i)
        else:
            print i
