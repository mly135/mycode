

import os

#当前工作目录
print(os.getcwd())

#切换目录
os.chdir('/Users/menglingyang/Desktop/')

#输出当前目录
print(os.getcwd())

#打开文件,内置方法 rb二进制方式 r文本方式
data  = open('培训.rtf')
#测试获取文件名
print(data.name)
# print(data)
print(data.readline(),end='')
# 重置指针
data.seek(0);

#data 对象可以作为迭代器
for foreach in data:
    print(foreach)

data.close();
