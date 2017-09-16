#coding=utf-8

###### 算是运算符

a = 2;
b= 3;
c=1;

print "1. a加b= ",a+b

print "2. a减b= ",a-b

print "3. a乘以b= ",a*b

print "4. a除以b= ", a/b

print "5. a的b次方", a**b

print "6. a除以b取余数", a%b

print "7. a除以b取余整", a//b



######赋值运算符

#赋值
a = 2

#a = a + 2
a+=2


#a = a -2
a-=2

#a = a * 2
a *= 2

#a = a /2
a /= 2

# a = a/ c
a /= c

# a = a**c
a **= c


# a = a 5=% c
a %= c

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print "1 - c 的值为：", c

c = a | b;  # 61 = 0011 1101
print "2 - c 的值为：", c

c = a ^ b;  # 49 = 0011 0001
print "3 - c 的值为：", c

c = ~a;  # -61 = 1100 0011
print "4 - c 的值为：", c

c = a << 2;  # 240 = 1111 0000
print "5 - c 的值为：", c

c = a >> 2;  # 15 = 0000 1111
print "6 - c 的值为：", c


###### 逻辑运算符    and  or   not

d = 0
e = 1
f = 2

print "0 and 1 结果为 0",d and f

print "0 or 1 结果为 1", d or f

print "not 表示非 0 and 1 结果为 1",not(d and f)


###### 成员运算符 in  和  not in

list = ["this","is","a","list"]


print "this 在list 里面","this" in list

print "tom 不再 list 里面" ,"tom" not in list


###### 身份运算符 is 和 is not  判断对象是否引用者同一个对象

print "d 和 f 是引用同一个对象 ？",d is f

print "d 和 f 不是引用用一个对象", d is not f

















