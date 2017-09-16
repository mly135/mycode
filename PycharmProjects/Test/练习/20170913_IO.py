#coding=utf-8


#内置输入函数 raw_input,参数是文本
# str = raw_input("请输入文本：")
# print "输入的文本为",str


#内置函数 input(),参数可以是表达式
#
# str1 = input("可以输入表达式，请输入")
# print "结果为：",str1


#file 对象
fo = open("foos.txt","wb")

print "文件名称",fo.name

print "是否已关闭",fo.closed

print "访问模式",fo.mode

fo.writelines("232321321我是一个中国人")
#关闭文件
fo.close()


#file 对象
readfile = open("foos.txt", "r+")
print readfile
str = readfile.read(10)
print "读取的字符串是 : ", str


#查找当前位置

wz = readfile.tell();
print "当前位置",wz

#设置当前指针位置
zz = readfile.seek(0,0);
print readfile.read(10)



#关闭文件
readfile.close()

#重命名，讲一个已存在的文件命名

import os

#文件重名
#os.rename("foos1.txt","foos.txt")

#移除文件
#os.remove("123")


#创建文件夹

os.mkdir("test")

os.chdir("test")

print os.getcwd()





