#coding=utf-8



result = ['zhangsan', 12, 'lisi', 13, 'wangwu', 14, 'zhaoliu', 15, 'mly', 16, 'chaochao', 17,["chaochao1",["chaochao2","chaochao3"]]]

#多曾嵌套，循环的不完善
#for i in result:
    # if isinstance(i, list):
    #     for j in i:
    #         print j
    # else:
    #     print i

# 循环遍历,使用递归方式
def foreach(li):
    for i in li:
        if isinstance(i, list):
            foreach(i)
        else:
            print (i)


# for j in result:
#     if isinstance(j, list):
#         foreach(j)
#     else:
#         print j

import mlytest


for j in result:
    if isinstance(j, list):
        mlytest.foreach(j)
    else:
        print (j)