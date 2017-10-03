

#打开一个当前目录的文件
file = open('test.py')

#循环file迭代器

for foreach in file:
    # print(foreach,end='')
    (name, speak)  = foreach.split(":")
    print(name, speak)


for foreach in file:
    # print(foreach,end='')
    print(foreach.split(":"))

file.close()
