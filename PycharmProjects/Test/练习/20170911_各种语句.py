# coding=utf-8

# if 任何非0 和 null 都是 true

a = 0

b = 1

c = 2

if a or b:
    print "a 或者 b 不同时是 0"
else:
    print "a 或者 b 有一个不是 0"


# while 循环语句

list = [1,2,3,4,5,6]

while len(list) > 0 :
    print list.pop()
else:
    print "循环结束"



# for 循环语句

for py in 'Python':     # 第一个实例
   print '当前字母 :', py

list = ['wo', 'shi', 'chaochao']

for li in list:
    print "list is " ,li

#下标方式
for index in range(len(list)):
    print list[index]
else:
    print "结束了"




# break 和 continue 关键字

for py in 'python':
    if py =='h':
        break
    print py



for py in 'python':
    if py =='h':
        continue
    print py

# pass 块
for py in 'python':
    if py =='h':
        pass
        print '这一块是pass'
    print py






