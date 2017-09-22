import mlytest

result = ['zhangsan', 12, 'lisi', 13, 'wangwu', 14, 'zhaoliu', 15, 'mly', 16, 'chaochao', 17,["chaochao1",["chaochao2","chaochao3"]]]

"""这个是最新的代码
请放心使用"""
mlytest.foreach(result,2, True)



# 循环遍历,使用递归方式
# def foreach(li, level=0, indent = False):
#     for i in li:
#         if isinstance(i, list):
#             foreach(i, level + 1, indent)
#         else:
#             if indent:
#                 for tab_stop in range(level):
#                     print("\t", end='')
#             print(i)
#
#foreach(result)