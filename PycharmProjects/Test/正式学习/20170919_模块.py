result = ['zhangsan', 12, 'lisi', 13, 'wangwu', 14, 'zhaoliu', 15, 'mly', 16, 'chaochao', 17,["chaochao1",["chaochao2","chaochao3"]]]
import sys
import mlytest



for j in result:
    if isinstance(j, list):
        mlytest.foreach(j)
    else:
        print (j)


print ("输出系统路径",sys.path)