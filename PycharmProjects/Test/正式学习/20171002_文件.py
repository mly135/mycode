#打开一个当前目录的文件
import os
try:
    file = open('test1.py')


#循环file迭代器
#设置参数1，仅匹配一个
# for foreach in file:
#     # print(foreach,end='')
#     if not foreach.find(":") == -1:
#         (name, speak)  = foreach.split(":",1)
#         print(name, speak)
#     else:
#         print(foreach)


#循环file迭代器
#设置参数1，仅匹配一个
    for foreach in file:
    # print(foreach,end='')
        try:
            (name, speak)  = foreach.split(":",1)
            print(name, speak)
        except ValueError:
            print("文件执行有异常")
    file.close()
except IOError:
    print("找不到文件")


