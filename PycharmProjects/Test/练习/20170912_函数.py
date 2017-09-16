#coding=utf-8

# 测试函数
def printname(str):
    "输出姓名"
    print str



# 调用函数

printname("I")


printname(str="love")



# 测试函数
def printNameAndAge(name,age):
    print "姓名：",name,"年龄",age

# 调用测试
printNameAndAge(age="23",name="张三")




# 测试函数  缺省参数
def printNameAndAge(name,age="25"):
    print "姓名：",name,"年龄",age

# 调用测试
printNameAndAge("李四")


#测试函数 不定长参数

def kebianHs(name,*other):
    print name
    for var in other:
        print var

#调用测试程序
kebianHs("张三","28","男")


#匿名函数

sum = lambda a,b: a+b


#调用匿名函数

print "匿名函数求和",sum(12,22)



