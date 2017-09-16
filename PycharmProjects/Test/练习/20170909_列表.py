#coding=utf-8

list = ["this","is","a","list"]

list1 = ["aaa","bbb"]

# 输出第一位
print(list[0])

# 输出列表长度
print(len(list))

# 后面加上 jok
list.append("jok")

# 弹出最后一个
print(list.pop())

# 列表直接拼接
list.extend(["jok","liu"])

# 按照名称移除元素
list.remove("jok")

# 某个位置添加元素
list.insert(2,"jok")

# 输出两次
print list*2

# 输出2开始，三个元素
print list[2:5]

# 列表拼接
print list+list1