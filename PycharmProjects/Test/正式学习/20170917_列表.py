#coding=utf-8

list = ["zhangsan","lisi","wangwu","zhaoliu"]

print list


list.append("chaochao")
print list


list.pop()
print list

list.extend(["mly","chaochao"])
print list

#给上边的列表添加年龄

age = [12,13,14,15,16,17,18]

print list[3]
#列表的数据可以类型不同
temp = []
i = 0



while i < len(list):
    temp.append(list[i])
    temp.append(age[i])
    i+=1
else:
    print temp

#for 循环遍历
for j in temp:
    print j

#while 遍历
k = 0
while k < len(temp):
    print temp[k]
    k+=1;
#测试插入，其他数据后移
#temp.insert(5,"测试位")
print temp



result = ['zhangsan', 12, 'lisi', 13, 'wangwu', 14, 'zhaoliu', 15, 'mly', 16, 'chaochao', 17,["chaochao1"["chaochao2","chaochao3"]]]



for i in result:
    if isinstance(i, list):
        for j in i:
            print j
    else:
        print i




