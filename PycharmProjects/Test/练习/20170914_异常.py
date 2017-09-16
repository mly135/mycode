#coding=utf-8

#成功示例
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()

#报错示例
try:
    fh = open("testfile", "w")
    fh.read(10)
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容读入文件成功"
    fh.close()

# 测试 try finally
try:
    try:
        i = 1/0
    finally:
        print "程序异常了"
except BaseException,error:
    print "被除数不能为0",error
else:
    print "运算成功"


# 手动抛出异常

# raise Exception("手动抛出异常","mly")



#手动创建异常类

class mlyException(RuntimeError):
    def __init__(self, age):
        self.age = age


try:
    raise mlyException("调用mly,让他抛出异常","超超")
except mlyException,error:
    print "调用了mlyException类",error